from random import randint
from time import sleep
import os 

lista = ('Pedra','Papel','Tesoura')
scorePlayer = 0
scorePC = 0
msg = ('Computador venceu','Jogador venceu','Empate')

def resultado(arg1, arg2):
    if lista[arg1] == lista[0]:
        if lista[arg2] == lista[0]:
            return 2
        elif lista[arg2] == lista[1]:
            return 0
        else:
            return 1
    elif lista[arg1] == lista[1]:
        if lista[arg2] == lista[1]:
            return 2
        elif lista[arg2] == lista[2]:
            return 0
        else:
            return 1
    elif lista[arg1] == lista[2]:
        if lista[arg2] == lista[2]:
            return 2
        elif lista[arg2] == lista[0]:
            return 0
        else:
            return 1

while True:
    computador = randint(0,2)
    os.system('cls')
    print('=-'*20) 
    print(f'Você = {scorePlayer}', end=" "*15)
    print(f'Computador = {scorePC}')
    print('=-'*20) 
    print('[0]Pedra\n[1]Papel\n[2]Tesoura')
    try:
        jogador = int(input('Qual a sua jogada? '))
        if jogador >= 3 or jogador < 0:
                print('Digite um valor valido.')
                sleep(1)
                continue

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!')
        sleep(1)
        print('=-'*20) 

        i = resultado(jogador,computador)
        print('Você jogou {} e o Computador jogou {}'.format(lista[jogador],lista[computador]))
        print('{}'.format(msg[i]))
        if i == 0:
            scorePC+=1
        elif i == 1:
            scorePlayer+=1

        print('=-'*20) 
    except:
        print('Digite um valor valido.')
        sleep(1)
        continue
    decisao = input('Quer continuar?\n[1]Sim\n[0]Não\n')
    if decisao == '1':

        continue
    elif decisao == '0' :
        os.system('cls')
        print(f'Resultado final\nJogador = {scorePlayer}',end=' '*15)
        print(f'Computador = {scorePC}')
        break
    else:       
        print('deu erro')