# Operações com Matrizes e Tensores

import numpy as np 
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# Criando arrays NumPy
array1 = np.array([(1,2),(3,4)], dtype = 'int32') 
array2 = np.array([(5,6),(7,8)], dtype = 'int32')
array3 = np.array([(2,7,2),(1,4,2),(9,0,2)], dtype = 'float32') 
array4 = np.array([[[1,2,3,4],[3,4,5,6]],[[5,6,7,8],[7,8,9,0]],[[1,3,5,7],[2,4,6,8]]]) 

print ("\nArray 1:") 
print (array1)
print ("\nArray 2:") 
print (array2)
print ("\nArray 3:") 
print (array3)
print ("\nArray 4:") 
print (array4)

# Operações com Matrizes e Tensores

# Multiplicação das matrizes 1 e 2
matrix_product = tf.matmul(array1, array2)

# Soma das matrizes 1 e 2
matrix_sum = tf.add(array1, array2)

# Cálculo do determinate da matriz 3
matrix_det = tf.linalg.det(array3)

# Calculando a raiz quadrada dos elementos do array 4
tf_tensor_3d = tf.convert_to_tensor(array4, dtype = tf.float64)
matrix_sqrt = tf.math.sqrt(tf_tensor_3d)

# Print
print ("\narray1 * array2:")
print (matrix_product) 
print ("\narray1 + array2:")
print (matrix_sum) 
print ("\nDeterminante do Array3 (Matriz): ")
print (matrix_det)
print ("\nRaiz Quadrada dos Elementos do Array 4: ")
print (matrix_sqrt)
print ("\n")
