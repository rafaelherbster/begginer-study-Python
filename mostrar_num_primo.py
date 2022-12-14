"""
mostrar os numeros primos dentro de um range
"""
import os

def primo():
    os.system('cls')
    n = int(input('Quais são os primos de 0 a '))
    for num in range(2,n+1):
        if all(num%i!=0 for i in range(2,num)):
            print(f'{num}', end= " ")


def checkprimo():
    os.system('cls')
    n = int(input('Digite o numero para saber se é primo '))
    if all(n%i!=0 for i in range(2,n)):
        print(f'{n} é número primo')
    else:
        print('Não é primo')


while True:
    escolha = input('\n[0]Mostrar primos dentro de um range\n[1]\
Checar se o numero é primo\n[2]Sair\n')
    if escolha == '0':
        primo()
    if escolha == '1':
        checkprimo()
    if escolha == '2':
        print('Voce saiu.')
        break
