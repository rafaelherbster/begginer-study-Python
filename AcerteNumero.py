from random import randint
import os

os.system('cls')
print('Tente advinhar o numero entre 0 e 100')
numGerado = randint(0,100)
tentativas = 0
while True:
    num = input("Digite um novo numero ")
    if int(num) == numGerado:
        tentativas+=1
        print(f'\nParabéns você acertou o numero certo em {tentativas} tentativas!')
        break
    elif int(num) < numGerado:
        tentativas+=1
        print(f'\nO numero que estou pensando é maior que {num}')
        continue
    elif int(num) > numGerado:
        tentativas+=1
        print(f'\nO numero que estou pensando é menor que {num}')
        continue