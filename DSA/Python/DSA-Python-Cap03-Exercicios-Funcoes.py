#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 3</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios - Métodos e Funções

# In[ ]:


# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      


# In[15]:


def pares():
    #imprime números pares
    x=[]
    for i in range(0,21,2):
        x.append(i)
    return(x)
pares()


# In[ ]:


# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string


# In[9]:


def maiuscula(string):
    #deita tudo maiusculo
    return(string.upper())


# In[10]:


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista


# In[11]:


def listfour(lista):
    lista.append(5)
    lista.append(6)
    return

liston = [1,2,3,4]
listfour(liston)
print(liston)


# In[ ]:


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos


# In[16]:


def listenha(arg1, *list):
    #imprime com um
    print("o argumento formal é: ", arg1)
    
    #imprime com vários
    for i in list:
        print("o argumento ", i, " é ", list)
    return

listenha('peixe')

listenha('peixe', 'boi', 'pizza', 'carangueijo')


# In[ ]:


# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles


# In[17]:


soma = lambda x,y : x+y

soma(2,5)


# In[18]:


# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)


# In[27]:


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x : x * 9/5 + 32, Celsius)
print (list(Fahrenheit))


# In[ ]:


# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário


# In[28]:


dic = {'peixe':'boi', 'ultra':'leve'}
dir(dic)


# In[31]:


# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
import pandas as pd
dir(pd)


# In[ ]:


# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd
file_name = "binary.csv"
 


# In[32]:


import pandas as pd
file_name = "binary.csv"

def descritivo(file_name):
    df = pd.read_csv(file_name)
    return df.describe()

descritivo(file_name)


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
