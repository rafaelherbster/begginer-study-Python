"""
mostrando matrizes de varias formas
"""
#duas colunas
# for i in range(0,4):
#    for n in range(0,4):
#        print(i,n)

#três colunas
# for i in range(0,3):
#     for n in range(0,3):
#         if n == 2:
#             print(f'[{i} {n}]', end='\n')
#         else:
#             print(f'[{i} {n}]', end=' ')

import string

num_letras = int(input('quantas letras? '))
num_linhas = 2*num_letras+1
meio = round((num_linhas**2)/2)
cont2 = 0
for l in range(num_letras):
    letra = string.ascii_lowercase[l]

for i in range(0,num_linhas):
    for n in range(0,num_linhas):
        cont2 += 1
        if n == num_linhas - 1:
            print(f'{letra}', end='\n')
        elif cont2 == meio+1:
            print('*', end=" ")
        else:
            print(f'{letra}', end=' ')