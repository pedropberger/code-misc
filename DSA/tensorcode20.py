# Regressão Linear com TensorFlow


# Imports
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# Modelo
class RegModel:
    def __init__(self):
        self.W = tf.Variable(16.0)
        self.b = tf.Variable(10.0)

    def __call__(self, x):
        return self.W * x + self.b

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

# Calculamos o erro usando uma função de custo
def loss(y, y_pred):
    return tf.reduce_mean(tf.square(y - y_pred))

# Função para executar o treinamento
def train(modelo, X, y, lr = 0.01):
    with tf.GradientTape() as t:
        current_loss = loss(y, modelo(X))

    derivada_W, derivada_b = t.gradient(current_loss, [modelo.W, modelo.b])
    modelo.W.assign_sub(lr * derivada_W)
    modelo.b.assign_sub(lr * derivada_b)

# Criamos o modelo
modelo = RegModel()

# Definimos listas vazias para W e b
Ws, bs = [], []

# Número de épocas (quantas vezes o modelo vai passar pelos dados)
epochs = 20

# Treinamento
print("\n")
for epoch in range(epochs):
    Ws.append(modelo.W.numpy()) 
    bs.append(modelo.b.numpy())

    current_loss = loss(y, modelo(X))

    train(modelo, X, y, lr = 0.1)
    
    print(f"Epoch {epoch}: Loss (Erro): {current_loss.numpy()}")

# Plot
plt.plot(range(epochs), Ws, 'r', range(epochs), bs, 'b')
plt.plot([TRUE_W] * epochs, 'r--', [TRUE_b] * epochs, 'b--')
plt.legend(['W Previsto', 'b Previsto', 'W Real', 'b Real'])
plt.show()

# Plot do valor "real"
plt.scatter(X, y, label = "Valor Real")

# Plot do valor "previsto" pelo nosso modelo
plt.scatter(X, modelo(X), label = "Valor Previsto")

plt.legend()
plt.show()


