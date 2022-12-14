import random
from time import sleep
import os

os.system('cls')
print('=-'*20)
print('GERADOR DE CPF'.center(40))
print('=-'*20)
n =input("Quantos CPF's você quer gerar? ")
print('Gerando novo cpf', end=' ')
for _ in range(3):
    print('.', end=' ')
    sleep(1)
contador_de_erros = 0


for _ in range(int(n)):
    def validar_1_dig(m,x1):
        contador = 0
        operação = 0
        soma = 0
        for i in m:
            soma += i*int(x1[contador]) 
            contador+=1

        operação += (soma*10)%11
        if operação>9:
            operação = 0
        return operação
    
    def validar_2_dig(m,x1):
        contador = 0
        operação = 0
        soma = 0
        for i in m:
            soma += i*int(x1[contador]) 
            contador+=1
            
        operação += (soma*10)%11
        if operação>9:
            operação = 0
        return operação

    multiplicador1 = []
    multiplicador2 = []
    cpf_usuario = ''

    for _ in range(9):
        cpf_usuario += str(random.randint(0,9))
    for i in range(10,1,-1):
        multiplicador1.append(i)
    for i in range(11,1,-1):
        multiplicador2.append(i)

    r1 = validar_1_dig(multiplicador1,cpf_usuario)
    cpf_usuario+=str(r1)
    r2 = validar_2_dig(multiplicador2,cpf_usuario)
    cpf_usuario+=str(r2)
    if len(cpf_usuario)<=11:
        print(f'\n Novo CPF gerado: {cpf_usuario}')
    else:
        contador_de_erros+=1
print('total de erros: ',contador_de_erros)
        
            