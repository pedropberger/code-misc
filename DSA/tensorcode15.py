# Usando Tensores Para Manipular Imagens - Slicing de Parte da Imagem

# Obs: Não executar este script no Titan. Executar localmente na sua máquina ou na VM.

import tensorflow as tf
import matplotlib.image as mp_image
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


# Preparando os dados
filename = "imagem.jpg"
input_image = mp_image.imread(filename)


# Dimensão
print ('\nDimensões da imagem: {}'.format(input_image.ndim))


# Shape
print ('\nShape da imagem: {}'.format(input_image.shape))


# Visualizando a imagem original
plt.imshow(input_image)
plt.show()


# Fatiando (slicing) a imagem

# Slice
slice = tf.slice(input_image,[10,0,0],[16,-1,-1])

print('\nSlice: ', slice)
print('\nShape do Slice: ', slice.shape)

plt.imshow(slice)
plt.show()

print('\n')
