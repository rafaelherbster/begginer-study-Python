"""
print itens duplicados de um lista


"""
lista = [0,1,2,3,3,4,4,5,6,7,7,8,'bola',9,'bola']
# repetidos = []

# for i in range(len(lista)):
#     for n in range(len(lista)):
#         if i == n:
#             pass
#         elif lista[i]==lista[n]:
#             if lista[i] in repetidos:
#                 pass
#             else:
#                 repetidos.append(lista[i])
#             break
#         else:  
#             pass
# for i in range(len(repetidos)):
#     print(f'{repetidos[i]}', end=' ')

var = set(x for x in lista if lista.count(x)>1)
# adcione elementos dentro de um conjunto e mostre-o
# para cada interavel dentro da lista 
# se a contagem desse elemento for maior que 1
for element in var:
    print(element, end=' ')
