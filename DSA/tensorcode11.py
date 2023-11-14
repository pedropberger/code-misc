# Definindo Tensors

# Tensores são as estruturas de dados básicas no TensorFlow. 
# Um tensor simplesmente identifica uma matriz ou lista multidimensional.

# Pode ser identificado por três parâmetros, rank, shape e type: 

# rank: Cada tensor é descrito por uma unidade de dimensionalidade chamada rank, que identifica o número de dimensões do tensor. 

# Shape: A forma de um tensor é o número de linhas e colunas que ele possui. 

# Type: É o tipo de dados atribuído aos elementos do tensor.


# Tensores Unidimensionais


# Criando um array Numpy
import numpy as np


# Criando array numpy unidimensional
tensor_1d = np.array([1.3,1,4.0,23.99])


# Print
print ('\nArray Numpy 1-D:', tensor_1d)
print ('\nElemento do Array Numpy 1-D no índice 0:', tensor_1d[0])
print ('\nElemento do Array Numpy 1-D no índice 2:', tensor_1d[2])

print ('\n')

# Criando tensores com TensorFlow
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


# Convertendo o array numpy para tensorflow
tf_tensor_1d = tf.convert_to_tensor(tensor_1d, dtype = tf.float64)


# Print
print ('\nTensor 1-D:', tf_tensor_1d)
print ('\nElemento do Tensor 1-D no índice 0:', tf_tensor_1d[0])
print ('\nElemento do Tensor 1-D no índice 2:', tf_tensor_1d[2])

print ('\n')




