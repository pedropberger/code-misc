#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 5</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios

# In[14]:


# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
               
roc1 = Rocket(15,10)
roc1.move_rocket(5,2)
roc1.print_rocket()


# In[ ]:





# In[3]:


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.


# In[50]:


class Pessoa():
    
    #definição inicial
    def __init__(self, nome, cidade, telefone, email):
        self.nome=nome
        self.cidade=cidade
        self.telefone=telefone
        self.email=email
        print("objeto criado maneiro")

        
    #imprimindo
    def __str__(self):
        return self.nome + " " + self.cidade
        
x=Pessoa("Pedro", "SMJ", 99915301, "pedropberger@gmail.com")

str(x)


# In[31]:


# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.


# In[57]:


class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
        
class MP3player(Smartphone):
    def __init__(self, capacidade, tamanho="ijij", interface="iujij"):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)
        
smt = Smartphone("321", "Led")

device = MP3player("doido")

print(device.capacidade)


# ### FIM

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
