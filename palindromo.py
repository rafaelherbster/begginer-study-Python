import os
os.system('cls')
# str1 = input('Digite uma string: ')
# rev_str = ''
# for i in range((len(str1)),0,-1):*
#     rev_str += str1[i-1]*
#* ESSA PARTE DO COD É O MESMO QUE USAR .join(reversed(arg))

# if str1 == rev_str:
#     print('É palindromo.')
# else:
#     print('Não é palindromo.')

def palindromo(s):
    rev_s = ''.join(reversed(s))
    if rev_s == s:
        return True
    return False

str1 = input('Digite uma string: ')
print(palindromo(str1))