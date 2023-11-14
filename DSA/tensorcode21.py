# Classificação com TensorFlow

# Vamos projetar e treiinar uma rede neural feed-forward simples para classificar imagens em 1 de 10 rótulos. 
# Usaremos keras, uma biblioteca de aprendizado profundo de alto nível, para definir e treinar nosso modelo. O Keras faz parte da biblioteca tensorflow, portanto, 
# a instalação separada não é necessária.


# Imports
import math
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# Usaremos o conjunto de dados FashionMNIST publicado pela Zalando Research, que é um pouco mais difícil do que o conjunto de dados escrito à mão do MNIST. 
# Este conjunto de dados contém imagens de itens de vestuário, como calças, casacos, bolsas etc. O conjunto de dados consiste em 60.000 imagens de treinamento e 10.000 imagens 
# de teste. Cada imagem é uma imagem em escala de cinza com tamanho 28x28 pixels. Existem 10 categorias no total e a cada rótulo é atribuído um número entre 0 e 9. 
# Os rótulos de classe correspondentes podem ser encontrados https://github.com/zalandoresearch/fashion-mnist#labels

# O Keras já vem com o conjunto de dados FashionMNIST e fará o download se ele ainda não existir em sua máquina. Vamos carregar o conjunto de dados e explorá-lo um pouco.

# Primeiro baixe e carregue o conjunto de dados
fashion_mnist = keras.datasets.fashion_mnist
(x_treino, y_treino), (x_teste, y_teste) = fashion_mnist.load_data()

# Vamos verificar quantas amostras existem no conjunto de treinamento e teste, seu tamanho e também as categorias.
print("\n")
print("Shape dos dados de treino (X): ", x_treino.shape)
print("Shape dos dados de treino (Y): ", np.unique(y_treino))
print("Shape dos dados de teste (X):  ", x_teste.shape)
print("\n")

# Agora vamos definir as classes (labels ou etiquetas)
class_names = {i:cn for i, cn in enumerate(['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']) }

# Função para o plot das imagens
def plot(images, labels, predictions = None):

    # Cria um grid de 5 colunas
    n_cols = min(5, len(images))
    n_rows = math.ceil(len(images) / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize = (n_cols + 3, n_rows + 4))
    
    # Checa se tem previsões para imprimir no Plot
    if predictions is None:
        predictions = [None] * len(labels)
        
    # Loop pelos dados para impressão no Plot
    for i, (x, y_true, y_pred) in enumerate(zip(images, labels, predictions)):
        ax = axes.flat[i]
        ax.imshow(x, cmap = plt.cm.binary)
        
        # Imprime o valor real (y)
        ax.set_title(f"L: {class_names[y_true]}")
        
        # Imprimie a previsão do modelo (y_pred)
        if y_pred is not None:
            ax.set_xlabel(f"Prev: {class_names[y_pred]}")
    
        ax.set_xticks([])
        ax.set_yticks([])

# Plot de algumas imagens
plot(x_treino[:15], y_treino[:15])   
plt.show()


