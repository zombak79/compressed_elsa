#NAdamS

import keras

from keras import backend
from keras import ops
from keras.src.backend.torch.core import *

class NadamS(keras.optimizers.Nadam):
 
    
    def update_step(self, gradient, variable, learning_rate, slicer=None):
        """Update step given gradient and the associated model variable."""
        var_dtype = variable.dtype
        lr = ops.cast(learning_rate, var_dtype)
        gradient = ops.cast(gradient, var_dtype)
  
        if slicer is None:
            slicer = torch.where(torch.count_nonzero(gradient, dim=1)!=0)
        else:
            slicer = (slicer, )
        
        nonzero_gradient = gradient[slicer]
        nonzero_variable = variable[slicer]
        
        local_step = ops.cast(self.iterations + 1, var_dtype)
        next_step = ops.cast(self.iterations + 2, var_dtype)
        decay = ops.cast(0.96, var_dtype)
        beta_1 = ops.cast(self.beta_1, var_dtype)
        beta_2 = ops.cast(self.beta_2, var_dtype)
        
        u_t = beta_1 * (1.0 - 0.5 * (ops.power(decay, local_step)))
        u_t_1 = beta_1 * (1.0 - 0.5 * (ops.power(decay, next_step)))
        u_product_t = ops.cast(self._u_product, var_dtype)

        u_product_t_1 = u_product_t * u_t_1
        beta_2_power = ops.power(beta_2, local_step)
        
        m = self._momentums[self._get_variable_index(variable)]
        v = self._velocities[self._get_variable_index(variable)]
        
        nonzero_m = m[slicer]
        nonzero_v = v[slicer]
        
        m = scatter_update_simple(m, slicer[0], nonzero_m + (nonzero_gradient - nonzero_m) * (1 - beta_1))
        v = scatter_update_simple(v, slicer[0], nonzero_v + (ops.square(nonzero_gradient) - nonzero_v) * (1 - beta_2))

        self.assign_add(
            m, ops.multiply(ops.subtract(gradient, m), (1 - beta_1))
        )
        self.assign_add(
            v, ops.multiply(ops.subtract(ops.square(gradient), v), (1 - beta_2))
        )
        m_hat = ops.add(
            ops.divide(ops.multiply(u_t_1, m), 1 - u_product_t_1),
            ops.divide(ops.multiply(1 - u_t, gradient), 1 - u_product_t),
        )
        v_hat = ops.divide(v, (1 - beta_2_power))

        self.assign_sub(
            variable,
            ops.divide(
                ops.multiply(m_hat, lr), ops.add(ops.sqrt(v_hat), self.epsilon)
            ),
        )
    
def scatter_update_simple(inputs, indices, updates):
    inputs = convert_to_tensor(inputs)
    indices = convert_to_tensor(indices, dtype="int64")
    updates = convert_to_tensor(updates)
    #print(indices)
    #indices = torch.transpose(indices, 0, 1)
    #print(tuple(indices))
    #print(inputs[indices].shape)
    inputs[indices] = updates
    inputs = Variable(inputs)
    return inputs

