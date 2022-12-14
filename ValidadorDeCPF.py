import os
from time import sleep


os.system('cls')

multiplicador1 =[]
multiplicador2 =[]

def validar_1_dig(m,x1,x2):
    contador = 0
    operação = 0
    soma = 0
    for i in m:
        soma += i*int(x1[contador]) 
        contador+=1

    operação += (soma*10)%11
    if str(operação) == x2:
        return True
    else:
        return False

def validar_2_dig(m,x1,x2):
    contador = 0
    operação = 0
    soma = 0
    for i in m:
            soma += i*int(x1[contador]) 
            contador+=1
    operação += (soma*10)%11
    if str(operação) == x2:
        return True
    else:
        return False

def cpf_9_dig(x):
    contador = 0
    cpf_9primeiros = ''
    for i in x:
        if contador < 9:
            cpf_9primeiros+=i
            contador+=1
        else:
            break
    return cpf_9primeiros

def cpf_10_dig(x):
    contador = 0
    cpf_10primeiros = ''
    for i in x:
        if contador < 10:
            cpf_10primeiros+=i
            contador+=1
        else:
            break
    return cpf_10primeiros

print('=-'*20)
print('VALIDADOR DE CPF'.center(40))
print('=-'*20)
print('INICIALIZANDO', end=' ')
sleep(1)
for _ in range(3):
    print('.', end=' ')
    sleep(1)

while True:
    cpf_usuario = input('\nDigite o cpf a ser validado sem pontos ou traços:\n')
    if cpf_usuario.isdigit() and len(cpf_usuario)==11:
        for i in range(10,1,-1):
            multiplicador1.append(i)
        for i in range(11,1,-1):
            multiplicador2.append(i)

        penultimo = cpf_usuario[-2]
        ultimo = cpf_usuario[-1]
        dig9 = cpf_9_dig(cpf_usuario)
        dig10 = cpf_10_dig(cpf_usuario)
        r1 = validar_1_dig(multiplicador1,dig9,penultimo)
        r2 = validar_2_dig(multiplicador2,dig10,ultimo)

        if r1 and r2 == True:
            print('CPF válido!')
            break   
        else:
            print('CPF inválido!')
            break  
    else: 
        print('Dado invalido!')
        sleep(1)
        os.system('cls')
        print('=-'*20)
        print('VALIDADOR DE CPF'.center(40))
        print('=-'*20)
        continue
        