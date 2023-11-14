# Regressão Linear com TensorFlow


# Imports
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Vamos definir um modelo de regressão linear. 

# Sabemos que um modelo linear é y = mx + c, onde m é a inclinação da reta e c é o intercepto. Portanto, os parâmetros deste modelo são m e c. 

# Em termos de aprendizado profundo, podemos chamá-los de peso e viés, respectivamente.

# O modelo abaixo possui atributos W e b que representam a inclinação e a interceptação, respectivamente. No código, o valor inicial foi definido como 16 e 10, 
# mas na prática eles são inicializados aleatoriamente. No TensorFlow, tudo o que um modelo aprende é definido usando tf.Variable. Isso significa que, ao longo da execução, 
# os valores dessas variáveis serão alterados, ou seja, são mutáveis.

# Em seguida, definimos a operação do nosso modelo na função __call__, que aceita uma entrada x. Semelhante à nossa equação acima, multiplicamos a entrada pelo peso W 
# e adicionamos o viés b. Ou no jargão da regressão linear, multiplicamos a entrada pela inclinação e adicionamos a interceptação.

# Observe que __call__ é uma função especial no Python que nos permite tratar um objeto como uma função, como veremos abaixo.

# Modelo
class RegModel:
    def __init__(self):
        self.W = tf.Variable(16.0)
        self.b = tf.Variable(10.0)

    def __call__(self, x):
        return self.W * x + self.b

# Instanciamos nosso modelo e passamos um valor 20. Como implementamos a função __call__, podemos tratar o objeto como uma função. E, como esperado, temos 330.
modelo = RegModel()
modelo(20)

# Por causa da execução ágil (eager execution), podemos ver imediatamente os resultados. O resultado do modelo é um tensor que não tem forma, ou seja, é um escalar do tipo float32. 
# No TF2, podemos facilmente converter para frente e para trás entre objetos tensores numpy e tensorflow. Como visto acima, o tensor também possui um valor numpy de 330.0. 
# Se queremos obter o valor numpy de um tensor, podemos chamar a função numpy() em um objeto tensor.

# Para este exemplo, vamos criar um conjunto de dados sintético. Geraremos os dados de modo que a inclinação da linha seja 3.0 e a interceptação seja 0.5. 
# Inicializamos o modelo com inclinação e interceptação muito diferentes e, se nosso modelo aprender alguma coisa, ele deve finalmente descobrir que a inclinação é 3.0 e o 
# viés é 0.5.

# Definindo valores "reais" para os pesos
TRUE_W = 3.0 # slope
TRUE_b = 0.5 # intercepto

# Número de exemplos
NUM_EXEMPLOS = 1000

# Amostramos X, isto é, as entradas, de uma distribuição normal, e também algum ruído. Em seguida, geramos y, ou seja, os resultados usando a fórmula de regressão linear 
# que vimos acima.

# Gera valores para x
X = tf.random.normal(shape = (NUM_EXEMPLOS,))

# Gera ruído
noise = tf.random.normal(shape = (NUM_EXEMPLOS,))

# Gera o valor "verdadeiro" de y
y = X * TRUE_W + TRUE_b + noise

# Vamos criar um plot do que temos até aqui

# Plot do valor "real"
plt.scatter(X, y, label = "Valor Real")

# Plot do valor "previsto" pelo nosso modelo
plt.scatter(X, modelo(X), label = "Valor Previsto")

plt.legend()
plt.show()





