import os
import torch

os.environ["KERAS_BACKEND"] = "torch"

import keras


class LayerELSA(keras.layers.Layer):
    def __init__(self, n_dims, n_items, device):
        super(LayerELSA, self).__init__()
        self.device = device
        self.A = torch.nn.Parameter(torch.nn.init.xavier_uniform_(torch.empty([n_dims, n_items])))

    def parameters(self, recurse=True):
        return [self.A]

    def track_module_parameters(self):
        for param in self.parameters():
            variable = keras.Variable(initializer=param, trainable=param.requires_grad)
            variable._value = param
            self._track_variable(variable)
        self.built = True

    def build(self):
        self.to(self.device)
        sample_input = torch.ones([self.A.shape[0]]).to(self.device)
        _ = self.call(sample_input)
        self.track_module_parameters()

    def call(self, x):
        A = torch.nn.functional.normalize(self.A, dim=-1)
        xA = torch.matmul(x, A)
        xAAT = torch.matmul(xA, A.T)
        return keras.activations.relu(xAAT - x)


class SparseLayerELSA(keras.layers.Layer):
    def __init__(self, n_items, n_dims, device, embeddings=None):
        super(SparseLayerELSA, self).__init__()
        self.device = device
        if embeddings is not None:
            print("create layer from provided embeddings")
            assert embeddings.shape[0] == n_items
            assert embeddings.shape[1] == n_dims
            self.A = torch.nn.Parameter(torch.from_numpy(embeddings))
        else:
            print("create new layer from scratch")
            self.A = torch.nn.Parameter(torch.nn.init.xavier_uniform_(torch.empty([n_items, n_dims])))
        self.W_list = [self.A]

    def parameters(self, recurse=True):
        return self.W_list

    def get_weights_(self):
        return keras.ops.vstack([self.W_list])

    def track_module_parameters(self):
        for param in self.parameters():
            variable = keras.Variable(  # keras.backend.Variable(
                initializer=param, trainable=param.requires_grad
            )
            variable._value = param
            self._track_variable(variable)
        self.built = True

    def build(self):
        self.to(self.device)
        sample_input = torch.ones([self.A.shape[0]]).to(self.device)
        _ = self.call(sample_input)
        self.track_module_parameters()

    def call(self, x):
        A = self.A
        A = torch.nn.functional.normalize(A, dim=-1)
        xA = torch.matmul(x, A)
        xAAT = torch.matmul(xA, A.T)
        return keras.activations.relu(xAAT - x)


class CompressedSparseLayerELSA(keras.layers.Layer):
    def __init__(self, n_items, n_dims, device, embeddings=None, n_vals=0, n_levels=None, level_dim=None):
        super(CompressedSparseLayerELSA, self).__init__()
        self.device = device
        self.n_vals = n_vals
        if embeddings is not None:
            print("create layer from provided embeddings")
            assert embeddings.shape[0] == n_items
            assert embeddings.shape[1] == n_dims
            self._A = torch.nn.Parameter(torch.from_numpy(embeddings))
        else:
            print("create new layer from scratch")
            self._A = torch.nn.Parameter(torch.nn.init.xavier_uniform_(torch.empty([n_items, n_dims])))
        self.W_list = [self._A]

        if level_dim is not None:
            assert n_levels is not None
            assert isinstance(level_dim, int)
            assert n_dims // n_levels == level_dim

        self.level_dim = level_dim
        self.n_levels = n_levels

    def A(self):
        A = self._A
        A = CompressedSparseLayerELSA.topk_mask(A, self.n_vals, dim=-1, n_levels=self.n_levels, level_dim=self.level_dim)
        A = torch.nn.functional.normalize(A, dim=-1)
        return A

    def parameters(self, recurse=True):
        return self.W_list

    def get_weights_(self):
        return keras.ops.vstack([self.W_list])

    def track_module_parameters(self):
        for param in self.parameters():
            variable = keras.Variable(  # keras.backend.Variable(
                initializer=param, trainable=param.requires_grad
            )
            variable._value = param
            self._track_variable(variable)
        self.built = True

    def build(self):
        self.to(self.device)
        sample_input = torch.ones([self._A.shape[0]]).to(self.device)
        _ = self.call(sample_input)
        self.track_module_parameters()

    def call(self, x):
        A = self._A
        A = CompressedSparseLayerELSA.topk_mask(A, self.n_vals, dim=-1, n_levels=self.n_levels, level_dim=self.level_dim)
        A = torch.nn.functional.normalize(A, dim=-1)
        xA = torch.matmul(x, A)
        xAAT = torch.matmul(xA, A.T)
        return keras.activations.relu(xAAT - x)

    @staticmethod
    def topk_mask(e: torch.Tensor, k: int, dim: int = -1, n_levels=None, level_dim=None) -> torch.Tensor:
        if len(e.shape) == 2 and k > 0 and level_dim is not None:
            n, _ = e.shape
            e_hierarichical = e.reshape([n, n_levels, level_dim])
            e_topk = torch.topk(torch.abs(e_hierarichical), k, dim)
            e_topk = torch.zeros_like(e_hierarichical).scatter(dim, e_topk.indices, e_topk.values) * torch.sign(e_hierarichical)
            return e_topk.reshape(e.shape)
        if k > 0:
            e_topk = torch.topk(torch.abs(e), k, dim)
            return torch.zeros_like(e).scatter(dim, e_topk.indices, e_topk.values) * torch.sign(e)
        return e
