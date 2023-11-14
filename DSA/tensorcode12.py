# Tensores Bidimensionais


# Criando um array Numpy
import numpy as np


# Criando array numpy bidimensional
tensor_2d = np.array([(1,2,3,4),(4,5,6,7),(8,9,10,11),(12,13,14,15)])


# Print
print ('\nArray Numpy 2-D:', tensor_2d)
print ('\nElemento do Array Numpy 2-D no índice [3][3]:', tensor_2d[3][3])
print ('\nElemento do Array Numpy 2-D no índice [0:2,0:2]:', tensor_2d[0:2,0:2])

print ('\n')

# Criando tensores com TensorFlow
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# Convertendo o array numpy para tensorflow
tf_tensor_2d = tf.convert_to_tensor(tensor_2d, dtype = tf.float64)


print ('\nTensor 2-D:', tf_tensor_2d)
print ('\nElemento do Tensor 2-D no índice [3][3]:', tf_tensor_2d[3][3])
print ('\nElemento do Tensor 2-D no índice [0:2,0:2]:', tf_tensor_2d[0:2,0:2])

print ('\n')




