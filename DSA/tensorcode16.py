# Usando Tensores Para Manipular Imagens - Transformações com Pacote tf.image

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
print ('\nDimensões da Imagem: {}'.format(input_image.ndim))

# Shape
print ('\nShape da Imagem: {}'.format(input_image.shape))


# Imprime a imagem
plt.imshow(input_image)
plt.show()


# Pacote tf.image
# https://www.tensorflow.org/api_docs/python/tf/image

# Ajusta o brilho da imagem
input_image_ajustada = tf.image.adjust_brightness(input_image, delta = 0.5)

plt.imshow(input_image_ajustada)
plt.show()


# Rotação da imagem com sua transposta
input_image_ajustada_transpose = tf.image.transpose(input_image_ajustada)

plt.imshow(input_image_ajustada_transpose)
plt.show()


# Inverte a posição da imagem
input_image_ajustada_transpose_inv = tf.image.random_flip_up_down(input_image_ajustada_transpose)

plt.imshow(input_image_ajustada_transpose_inv)
plt.show()

