"""
Write a Sort function to sort the elements in a list
"""
from time import sleep
import os

lista = []
while True:
        decisao = input('\nO que você quer fazer?\n[0]Sair\n[1]Adcionar item a '
        'lista\n[2]Ordenar: Crescente\n[3]Ordenar: Decrescente\n')
        # '[4]Mostrar lista ')
        #lista[;;-1] leia a lista de forma reversa a como foi adcionada

        if decisao.isnumeric() == False or int(decisao)>3:
            os.system('cls')
            print('Você não escolheu uma opção válida.')
            continue

        if decisao == '0':
            os.system('cls')
            print('Você saiu. ')
            break

        if decisao == '1':
            os.system('cls')
            num  = input('Digite o numero que vai ser adicionado à lista: ')
            lista.append(num)
            continue

        if decisao == '2':
            if len(lista) == 0:
                os.system('cls')
                print('Não foi possivel completar a ação, preencha sua lista!')
                sleep(2)
                continue
            else: 
                lista.sort()
                os.system('cls')
                print('Sua lista atual é:')
                for i in lista:
                    print(f'{i}', end= ' ')
                print('\n')
                continue

        if decisao == '3':
            if len(lista) == 0:
                os.system('cls')
                print('Não foi possivel completar a ação, preencha sua lista!')
                sleep(2)
                continue
            else: 
                lista.sort(reverse= True)
                os.system('cls')
                print('Sua lista atual é:')
                for i in lista:
                    print(f'{i}', end= ' ')
                print('\n')
                continue

 