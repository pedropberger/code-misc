# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")


print("\n \n Selecione o número da operação desejada:","\n \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")
oper = int(input("Digite o número da operação: "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

def calculadora (oper, n1, n2):
    if oper == 1:
        return(n1 + n2)
    elif oper == 2:
        return(n1-n2)
    elif oper == 3:
        return(n1*n2)
    else:
        return(n1/n2)
    
print("O resultado é ", calculadora(oper, n1, n2))
