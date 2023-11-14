# Tensores com 3 dimensões

import numpy as np 
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


# Cria o array tridimensional
# Dimensões: (panel, row, col)
tensor_3d = np.array([[[1,2,3,4],[3,4,5,6]],[[5,6,7,8],[7,8,9,0]],[[1,3,5,7],[2,4,6,8]]]) 

#   |       -- axis-2 ->
#   |    |
#   |  axis-1 [1,2,3,4]
#   |    |    [3,4,5,6]
#   |    V
# axis-0
#   |      -- axis-2 ->
#   |    |
#   |  axis-1 [5,6,7,8]
#   |    |    [7,8,9,0]
#   |    |
#   |    V -- axis-2 ->
#   |    |
#   |  axis-1 [1,3,5,7]
#   |    |    [2,4,6,8]
#   V    V


# Print
print ('\nArray Numpy 3-D:', tensor_3d)


# Shape do Array
print ('\nShape do Array:', tensor_3d.shape)


# Elementos do array 3-D
print ('\nElemento do Array Numpy 3-D no índice [0,0,0]:', tensor_3d[0,0,0])
print ('\nElemento do Array Numpy 3-D no índice [0,1,1]:', tensor_3d[0,1,1])
print ('\nElemento do Array Numpy 3-D no índice [:, 0, 0]:', tensor_3d[:, 0, 0])


# Convertendo o array numpy para tensorflow
tf_tensor_3d = tf.convert_to_tensor(tensor_3d, dtype = tf.float64)


print ('\nTensor 3-D:', tf_tensor_3d)
print ('\nElemento do Tensor 3-D no índice [0,0,0]:', tf_tensor_3d[0,0,0])
print ('\nElemento do Tensor 3-D no índice [0,1,1]:', tf_tensor_3d[0,1,1])
print ('\nElemento do Tensor 3-D no índice [:, 0, 0]:', tf_tensor_3d[:, 0, 0])


# Shape do Tensor
print ('\nShape do Tensor:', tf_tensor_3d.shape)

print ('\n')

