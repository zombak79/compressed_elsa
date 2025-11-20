import math
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.utils.data import Dataset, DataLoader, random_split
from tqdm import tqdm

def l2_normalize(x: torch.Tensor, dim: int = -1) -> torch.Tensor:
    return x / x.norm(dim=dim, keepdim=True)


class CompresSAE(nn.Module):
    def __init__(self, input_dim: int, embedding_dim: int, k: int):
        super().__init__()
        self.k = k
        self.embedding_dim = embedding_dim
        self.encoder_w = nn.Parameter(nn.init.kaiming_uniform_(torch.empty([input_dim, embedding_dim])))
        self.encoder_b = nn.Parameter(torch.zeros(embedding_dim))
        self.decoder_w = nn.Parameter(nn.init.kaiming_uniform_(torch.empty([embedding_dim, input_dim])))
        self.normalize_decoder()

    def encode(self, x: torch.Tensor, apply_activation: bool = True) -> torch.Tensor:
        e_pre = l2_normalize(x) @ self.encoder_w + self.encoder_b
        return self.topk_mask(e_pre, self.k) if apply_activation else e_pre

    def decode(self, e: torch.Tensor) -> torch.Tensor:
        return e @ self.decoder_w

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.decode(self.encode(x))

    @torch.no_grad()
    def normalize_decoder(self) -> None:
        self.decoder_w.data = l2_normalize(self.decoder_w.data)
        if self.decoder_w.grad is not None:
            self.decoder_w.grad -= (self.decoder_w.grad * self.decoder_w.data).sum(-1, keepdim=True) * self.decoder_w.data

    @staticmethod
    def topk_mask(e: torch.Tensor, k: int, dim: int = -1) -> torch.Tensor:
        e_topk = torch.topk(torch.abs(e), k, dim)
        return torch.zeros_like(e).scatter(dim, e_topk.indices, e_topk.values) * torch.sign(e)

    def compute_loss_dict(self, x: torch.Tensor) -> dict[str, torch.Tensor]:
        e_pre = self.encode(x, apply_activation=False)
        e, e_4k = self.topk_mask(e_pre, self.k), self.topk_mask(e_pre, min(self.k, 4 * self.k))
        x_out, x_out_4k = self.decode(e), self.decode(e_4k)
        losses = {
            "L2": (x_out - x).pow(2).mean(),
            "L2_4k": (x_out_4k - x).pow(2).mean(),
            "L1": e.abs().sum(-1).mean(),
            "L0": (e != 0).float().sum(-1).mean(),
            "Cosine": (1 - F.cosine_similarity(x, x_out, 1)).mean(),
            "Cosine_4k": (1 - F.cosine_similarity(x, x_out_4k, 1)).mean(),
        }
        losses["Loss"] = losses["Cosine"] + losses["Cosine_4k"] / 8
        return losses

    def train_step(self, optimizer: optim.Optimizer, batch: torch.Tensor) -> dict[str, torch.Tensor]:
        losses = self.compute_loss_dict(batch)
        optimizer.zero_grad()
        losses["Loss"].backward()
        self.normalize_decoder()
        optimizer.step()
        return losses

class EmbeddingDataset(Dataset):
    """
    Wrap a 2D numpy array (N, D). Returns (x, x) pairs for AE training.
    """
    def __init__(self, embeddings: np.ndarray, dtype=torch.float32):
        assert isinstance(embeddings, np.ndarray) and embeddings.ndim == 2
        self.x = torch.from_numpy(embeddings).to(dtype)

    def __len__(self):
        return self.x.shape[0]

    def __getitem__(self, idx):
        x = self.x[idx]
        return x, x

@torch.no_grad()
def evaluate(model, loader, device: torch.device):
    model.eval()
    agg = {}
    n = 0
    for xb, _ in loader:
        xb = xb.to(device, non_blocking=True)
        losses = model.compute_loss_dict(xb)
        bs = xb.size(0)
        for k, v in losses.items():
            agg[k] = agg.get(k, 0.0) + float(v.item()) * bs
        n += bs
    return {k: v / max(n, 1) for k, v in agg.items()}

def make_loader(
    embeddings: np.ndarray,
    batch_size: int = 256,
    val_ratio: float = 0.1,
    num_workers: int = 0,
    seed: int = 42,
):
    g = torch.Generator().manual_seed(seed)
    ds = EmbeddingDataset(embeddings)

    train_loader = DataLoader(
        ds, batch_size=batch_size, shuffle=True,  # ← reshuffles each epoch
        drop_last=False, num_workers=num_workers, pin_memory=True
    )
    return train_loader

def make_loaders(
    embeddings: np.ndarray,
    batch_size: int = 256,
    val_ratio: float = 0.1,
    num_workers: int = 0,
    seed: int = 42,
):
    g = torch.Generator().manual_seed(seed)
    ds = EmbeddingDataset(embeddings)
    n_val = max(1, int(math.floor(len(ds) * val_ratio)))
    n_train = len(ds) - n_val
    
    if val_ratio == 0:
        train_ds, val_ds = ds, ds
    else:
        train_ds, val_ds = random_split(ds, [n_train, n_val], generator=g)

    train_loader = DataLoader(
        train_ds, batch_size=batch_size, shuffle=True,  # ← reshuffles each epoch
        drop_last=False, num_workers=num_workers, pin_memory=True
    )
    val_loader = DataLoader(
        val_ds, batch_size=batch_size, shuffle=False,
        drop_last=False, num_workers=num_workers, pin_memory=True
    )
    return train_loader, val_loader

def train(
    model,
    train_loader,
    val_loader,
    epochs: int = 10,
    lr: float = 1e-3,
    weight_decay: float = 0.0,
    device: str | torch.device = "cuda" if torch.cuda.is_available() else "cpu",
    grad_clip: float | None = None,
    verbose: bool = True,
    early_stopping = 0,
    optimizer = None,
    scheduler = None,
    annealing = [],
):
    device = torch.device(device)
    model = model.to(device)
    if len(annealing)>0:
        print(f"Using annealing startegy {annealing}")
    else:
        print("No annealing startegy.")
    if optimizer is None:
        optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    
    best_val = float("inf")
    best_state = None
    final_k = model.k
    early_stop = 0
    for epoch in (pbar := tqdm(range(1, epochs + 1))):
        if len(annealing)>0:
            if epoch >= len(annealing):
                model.k = final_k
                print(f"setting k for final training to {model.k}")
            else:
                model.k = annealing[epoch-1]
                print(f"setting k to {model.k}")
        model.train()
        if scheduler is not None:
            scheduler.step()
        run_loss = 0.0
        n = 0
        for xb, _ in train_loader:
            xb = xb.to(device, non_blocking=True)
            losses = model.train_step(optimizer, xb)
            if grad_clip is not None:
                torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
            # Note: model.train_step() already zero_grads, backward, normalize_decoder, and optimizer.step()

            bs = xb.size(0)
            run_loss += float(losses["Loss"].item()) * bs
            n += bs

        train_loss = run_loss / max(n, 1)
        val_metrics = evaluate(model, val_loader, device)
        val_loss = val_metrics["Loss"]

        if val_loss < best_val:
            best_val = val_loss
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
        else:
            early_stop += 1
        
        if verbose:
            pbar.set_description(f"train Loss {train_loss:.6f} | "+
                  f"val Loss {val_loss:.6f} | val Cos {val_metrics['Cosine']:.6f} | "+
                  f"val L2 {val_metrics['L2']:.6f}"
            )

        if early_stopping!=0 and early_stop > early_stopping:
            print("stopping early")
            break
            
    

    if best_state is not None:
        model.load_state_dict(best_state)
    return model, {"best_val": best_val}