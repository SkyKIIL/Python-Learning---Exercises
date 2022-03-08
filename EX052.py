print('\033[1;7;37m+++++IDENTIFICADOR DE NÚMEROS PRIMOS+++++\033[m')
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print(end='\033[32m')
        tot += 1
    else:
        print(end='\033[31m')
    print(end=' 'f'{c}')
print(f'\n\033[1;33mO número {n} foi divisível {tot} vezes!')
if tot == 2:
    print('Portanto ele é PRIMO!')
else:
    print('Portanto ele NÃO é PRIMO!')
