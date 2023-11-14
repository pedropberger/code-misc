# Números Randômicos com Distribuição Normal e Uniforme

# Obs: Não executar este script no Titan. Executar localmente na sua máquina ou na VM.

import tensorflow as tf
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# Distribuição Normal
# Cria um tensor de shape [100] constituído por valores aleatórios normalmente distribuídos, com média 0 e desvio padrão 1.
norm = tf.random.normal([100], mean = 0, stddev = 1)
print('\nTensor com Dados Aleatórios e Distribuição Normal:', norm)
print('\nShape:', norm.shape)
plt.hist(norm)
plt.show()  


# Distribuição Uniforme
# Cria um tensor de shape [100] constituído por valores aleatórios,entre 0 e 1
uniform = tf.random.uniform([100], minval = 0, maxval = 1)
print('\nTensor com Dados Aleatórios e Distribuição Uniforme:', uniform)
print('\nShape:', uniform.shape)
plt.hist(uniform)
plt.show() 

print('\n')




