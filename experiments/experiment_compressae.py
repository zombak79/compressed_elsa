import os
import torch
import argparse
import subprocess

import keras

from _datasets.utils import Evaluation, fast_pruning, get_sparse_matrix_from_dataframe
import numpy as np
import pandas as pd


from recommenders.elsa_models import CompressedSparseKerasELSA

from _datasets.config import config

from time import time

from utils.compressae import CompresSAE, train, make_loaders

parser = argparse.ArgumentParser()

parser.add_argument("--seed", default=42, type=int, help="Random seed")

parser.add_argument("--device", default=0, type=int, help="Default device to run on")

parser.add_argument("--factors", default=4096, type=int, help="Number of model factors")
parser.add_argument("--batch_size", default=1024, type=int, help="Batch size for model training")
parser.add_argument("--top_k", default=16, type=int, help="Top k of prdictions considered during training. Works only in finetuning mode.")
parser.add_argument("--user_embeddings", default="False", type=str, help="Use user embeddings for training.")
parser.add_argument("--vals", default="", type=str)

parser.add_argument("--lr", default=0.001, type=float, help="Learning rate for model training, only if scheduler is none")
parser.add_argument("--weight_decay", default=0.0, type=float, help="weight decay for l2 regularozation of weights during training")

parser.add_argument("--epochs", default=10, type=int, help="Total epochs of model training")

parser.add_argument("--weights", default="elsa", type=str, help="model: [elsa]")

parser.add_argument("--dataset", default="", type=str, help="dataset. For list of datasets leave this parameter blank.")
parser.add_argument("--validation", default="false", type=str, help="Use validation split: true/false")

parser.add_argument("--pu", default=1, type=int, help="User pruning aplied on training data.")
parser.add_argument("--pi", default=1, type=int, help="Item pruning aplied on training data.")

parser.add_argument("--max_output", default=None, type=int, help="Max number of items on output for super sparse method.")

parser.add_argument("--flag", default="none_compressae", type=str, help="flag for distinction of experiments, default none")

args = parser.parse_args([] if "__file__" not in globals() else None)
args.vals = [int(x) for x in args.vals.split(" ")] if len(args.vals) > 0 else []

os.environ["KERAS_BACKEND"] = "torch"
os.environ["CUDA_VISIBLE_DEVICES"] = f"{args.device}"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

try:
    seed = [int(x[1:]) for x in args.weights.split(".")[0].split("_") if x[0] == "s"][0]
    print(f"Succesfully extracted seed from args.weights ({seed}). Ignoring argument args.seed ({args.seed}).")
    args.seed = seed
except:  # noqa: E722
    print(f"Cannot extract seed from args.weights. Using args.seed ({args.seed}) instead.")


if __name__ == "__main__":
    folder = f"results/{str(pd.Timestamp('today'))} {9*int(1e6)+np.random.randint(999999)}".replace(" ", "_")
    if not os.path.exists(folder):
        os.makedirs(folder)
    vargs = vars(args)
    vargs["cuda_or_cpu"] = DEVICE
    pd.Series(vargs).to_csv(f"{folder}/setup.csv")
    print(folder)
    print(f"Setting random seed to {args.seed}")
    torch.manual_seed(args.seed)
    keras.utils.set_random_seed(args.seed)
    np.random.seed(args.seed)

    print(args)
    try:
        assert args.dataset in config.keys()
    except:
        print(f"Dataset must be one of {list(config.keys())}.")
        raise

    dataset, params = config[args.dataset]
    params["random_state"] = args.seed
    print(f"Loding dataset {args.dataset} with params {params}")
    dataset.load_interactions(**params)
    print(dataset)

    if args.validation == "true":
        print("creating validation evaluator")
        val_evaluator = Evaluation(dataset, "validation")
        df = fast_pruning(dataset.train_interactions, args.pu, args.pi)
    else:
        df = fast_pruning(dataset.full_train_interactions, args.pu, args.pi)

    X = get_sparse_matrix_from_dataframe(df)

    print(f"Interaction matrix: {repr(X)}")

    print("creating test evaluator")
    test_evaluator = Evaluation(dataset, "test")

    print()
    print(f"Loading model {args.weights}")
    A = np.load(args.weights)
    print(f"Loaded array of shape {A.shape}, dtype {A.dtype}")

    train_loader, val_loader = make_loaders(
        X @ A if args.user_embeddings == "True" else A, batch_size=args.batch_size, val_ratio=0, num_workers=0, seed=args.seed
    )

    model = CompresSAE(input_dim=A.shape[1], embedding_dim=args.factors, k=args.top_k)

    start = time()
    model, info = train(
        model, train_loader, val_loader, epochs=args.epochs, lr=args.lr, weight_decay=args.weight_decay, grad_clip=None, early_stopping=100, annealing=args.vals
    )
    train_time = time() - start
    print("Best val Loss:", info["best_val"])

    A_csae = model.encode(torch.from_numpy(A).cuda()).cpu().detach().numpy()

    model = CompressedSparseKerasELSA(X.shape[1], args.factors, df.item_id.cat.categories, device=DEVICE, embs=A_csae)

    df_preds = model.predict_df(test_evaluator.test_src)
    results = test_evaluator(df_preds)

    print(results)
    # ks = list(f.history.keys())
    # dc = {k:np.array([(f.history[k]) for f in fits]).flatten() for k in ks}
    # dc["epoch"] = np.arange(len(dc[list(dc.keys())[0]]))+1
    # df[list(df.columns[-1:])+list(df.columns[:-1])]
    # df = pd.DataFrame(dc)

    pd.DataFrame().to_csv(f"{folder}/history.csv")
    # print("history file written")

    pd.Series(results).to_csv(f"{folder}/result.csv")
    print("results file written")

    pd.Series(train_time).to_csv(f"{folder}/timer.csv")
    # print("timer written")

    out = subprocess.check_output(["nvidia-smi"])

    with open(os.path.join(f"{args.dataset}_{args.flag}.log"), "w") as f:
        f.write(out.decode("utf-8"))
