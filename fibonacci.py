#mostre o enesimo termo da sequencia fibonacci, 
# metodo recursivo

# def fibonacci(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# import os
# from time import process_time

# os.system('cls')

# n = int(input('Digite o enésimo termo da sequencia fibonacci\
#  a ser mostrado: '))
# print(f'O {n}° termo na sequencia'
#  f' de Fibonacci é {fibonacci(n)}.\n'
#  f'Essa resposta foi dada em {process_time()} segundos.')

# # Define a function to generate Fibonacci numbers
# def fibonacci(n):
#   # Initialize the first two numbers in the sequence
#   a = 0
#   b = 1

#   # Loop through the sequence and calculate each number
#   for i in range(n-1):
#     # Calculate the next number in the sequence
#     c = a + b
#     # Print the current number
#     print(f'{c}', end=' ')
#     # Shift the numbers in the sequence
#     a = b
#     b = c

# # Call the function to generate and print the first n Fibonacci numbers
# print(f'0', end=' ')
# print(f'1', end=' ')
# fibonacci(50)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = fibonacci(n-1)
        b = fibonacci(n-2)
        return a + b

for i in range(0,7):
    print(fibonacci(i),i)


