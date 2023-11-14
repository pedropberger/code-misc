# Regressão Logística

# Com Regressão logística, buscamos uma função que nos diga qual é a probabilidade de um elemento pertencer a uma classe. 
# A aprendizagem supervisionada é configurada como um processo iterativo de otimização dos pesos. Estes são então modificados com base no desempenho do modelo.
# De fato, o objetivo é minimizar a função de perda, que indica o grau em que o comportamento do modelo se desvia do desejado. 
# O desempenho do modelo é então verificado em um conjunto de teste, consistindo em imagens diferentes das de treinamento.

# Os passos básicos do treinamento que vamos implementar são os seguintes: 

# 1- Os pesos são inicializados com valores aleatórios seguindo uma distribuição normal.
# 2- Para cada elemento do conjunto de treino é calculado o erro, ou seja, a diferença entre a saída prevista e a saída real. Este erro é usado para ajustar os pesos. 
# 3- O processo é repetido em todos os exemplos do conjunto de treinamento até que o erro em todo o conjunto de treinamento não seja inferior a um certo limite, 
# ou até que o número máximo de iterações seja atingido.

# Nosso objetivo é a classificação de imagens de peças de vestuário.
# Classes do dataset fashion_mnist - ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# Importando pacotes
import math
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Importando dataset 
(x_treino, y_treino), (x_teste, y_teste) = fashion_mnist.load_data()

# Normalizando as imagens
x_treino, x_teste = x_treino/255., x_teste/255.

# Ajusta o shape de x de 28x28 para 784
x_treino = tf.reshape(x_treino, shape = (-1, 784))
x_teste  = tf.reshape(x_teste, shape = (-1, 784))

# Construindo o Modelo

# Definindo os pesos, variáveis W e b
# Inicializando os Coeficientes de Forma Randômica com Distribuição Normal
pesos = tf.Variable(tf.random.normal(shape = (784, 10), dtype = tf.float64))
vieses  = tf.Variable(tf.random.normal(shape = (10,), dtype = tf.float64))

# Função para o cálculo do resultado da regressão logísitica
# g(y) = β(x) + βo  
def logistic_regression(x):
    lr = tf.add(tf.matmul(x, pesos), vieses)
    return lr

# Minimizando o erro usando cross entropy (Função de Custo).
# A fim de treinar nosso modelo, devemos definir como identificar a precisão. 
# Nosso objetivo é tentar obter valores de parâmetros W e b que minimizem o valor da métrica que indica quão ruim é o modelo.
# Diferentes métricas calculam o grau de erro entre a saída desejada e as saídas de dados de treinamento. 
# Uma medida comum de erro é o erro quadrático médio ou a Distância Euclidiana Quadrada. No entanto, existem algumas descobertas de pesquisa que sugerem usar outras 
# métricas para uma rede neural. Neste exemplo, usamos a chamada função de erro de entropia cruzada.
def cross_entropy(y_true, y_pred):
    y_true = tf.one_hot(y_true, 10)
    loss = tf.nn.softmax_cross_entropy_with_logits(labels = y_true, logits = y_pred)
    return tf.reduce_mean(loss)

# Otimizando a Cost Function
# Em seguida, devemos minimizá-lo usando o algoritmo de otimização de descida de gradiente:
def grad(x, y):
    with tf.GradientTape() as tape:
        y_pred = logistic_regression(x)
        loss_val = cross_entropy(y, y_pred)
    return tape.gradient(loss_val, [pesos, vieses])

# Hiperparâmetros
n_batches = 10000
learning_rate = 0.01
batch_size = 128

# Cria o otimizador usando SGD (Stochastic Gradient Descent)
optimizer = tf.optimizers.SGD(learning_rate)

# Função para o cálculo da Acurácia
def accuracy(y_true, y_pred):
    y_true = tf.cast(y_true, dtype = tf.int32)
    preds = tf.cast(tf.argmax(y_pred, axis = 1), dtype = tf.int32)
    preds = tf.equal(y_true, preds)
    return tf.reduce_mean(tf.cast(preds, dtype = tf.float32))

# Preparando batches de dados de treino
dataset_treino = tf.data.Dataset.from_tensor_slices((x_treino, y_treino))
dataset_treino = dataset_treino.repeat().shuffle(x_treino.shape[0]).batch(batch_size)

print ("\nIniciando o Treinamento!")

# Ciclo de treinamento
for batch_numb, (batch_xs_treino, batch_ys_treino) in enumerate(dataset_treino.take(n_batches), 1):

    # Calcula os gradientes
    gradientes = grad(batch_xs_treino, batch_ys_treino)

    # Otimiza os pesos com o valor do gradiente
    optimizer.apply_gradients(zip(gradientes, [pesos, vieses]))

    # Faz uma previsão
    y_pred = logistic_regression(batch_xs_treino)

    # Calcula o erro
    loss = cross_entropy(batch_ys_treino, y_pred)

    # Calcula a acurácia
    acc = accuracy(batch_ys_treino, y_pred)

    # Print
    print("Número do Batch: %i, Erro do Modelo: %f, Acurácia em Treino: %f" % (batch_numb, loss, acc))

print ("\nTreinamento concluído!")

# Testando o Modelo

# Preparando os dados de teste
dataset_teste = tf.data.Dataset.from_tensor_slices((x_teste, y_teste))
dataset_teste = dataset_teste.repeat().shuffle(x_teste.shape[0]).batch(batch_size)

print ("\nIniciando a Avaliação com Dados de Teste. Por favor aguarde!")

# Loop pelos dados de teste, previsões e cálculo da acurácia
for batch_numb, (batch_xs_teste, batch_ys_teste) in enumerate(dataset_teste.take(n_batches), 1):
    y_pred = logistic_regression(batch_xs_teste)
    acc = accuracy(batch_ys_teste, y_pred)
    acuracia = tf.reduce_mean(tf.cast(acc, tf.float64))

print("\nAcurácia em Teste: %f" % acuracia)

print("\nFazendo Previsão de Uma Imagem:")

# Obtendo os dados de algumas imagens
dataset_teste = tf.data.Dataset.from_tensor_slices((x_teste, y_teste))
dataset_teste = dataset_teste.repeat().shuffle(x_teste.shape[0]).batch(1)

# Fazendo previsões
for batch_numb, (batch_xs, batch_ys) in enumerate(dataset_teste.take(1), 1):
    # print("\nImagem:", batch_xs)
    print("\nClasse Real:", batch_ys)
    y_pred = tf.math.argmax(logistic_regression(batch_xs), axis = 1)
    # y_pred = logistic_regression(batch_xs)
    print("Classe Prevista:", y_pred)

print("\nExemplo de Peso e Viés Aprendidos:")
print(pesos[2,9])
print(vieses[2])
print("\n")




