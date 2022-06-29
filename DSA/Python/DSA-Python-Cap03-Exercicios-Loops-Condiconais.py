#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 3</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios - Loops e Condiconais

# In[1]:


# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de" descanso", caso contrário imprima na tela "Você precisa trabalhar!"


# In[ ]:


print('qual o dia da semana?')
x = input()

if x == ("Domingo") or x==("Sábado"):
  print("Hoje é dia de descanso")
#elif x == ("Sábado"):
#  print("Hoje é dia de descanso") 
else:
  print("Você precisa trabalhar!")


# In[2]:


# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista


# In[6]:


lista = ["ovos", "farinha", "leite", "maças", "morango"]

for i in lista:
    if i == ("morango"):
        print("morango ta na lista")


# In[ ]:


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista


# In[24]:


tupla = (1,2,3,4)

print(tupla)
x=[]
for i in tupla:
    x.append(i*2)
print(x)


# In[ ]:


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela


# In[27]:


for i in range(100,151,2):
    x.append(i)
print(x)


# In[ ]:


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela


# In[28]:


temperatura = 40

while temperatura > 35:
    print(temperatura)
    temperatura-=1


# In[ ]:


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa


# In[31]:


contador = 0
while contador < 100:
    print(contador)
    if contador == 23:
        break
    contador+=1


# In[ ]:


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista


# In[32]:


list=[]
var = 4
while var <= 20:
    if var%2==0:
        list.append(var)
    var+=1
print(list)


# In[ ]:


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)


# In[35]:


x=[]
for i in range(5,45,2):
    x.append(i)
print(x)


# In[ ]:


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30
print('Vista roupas leves.')
else
    print('Busque seus casacos.')


# In[37]:


temperatura = float(input('Qual a temperatura?'))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')


# In[38]:


# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 


# In[43]:


count=0
for i in frase:
    if i =='r':
        count+=1
print("O r aparece %s vezes" %(count))


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
