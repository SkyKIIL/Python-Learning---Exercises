"""print('   \033[1;7;32m+++++GERADOR DE P.A+++++\033[m')
print('=-=' * 10)
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
while cont <= 10:
    if cont < 10:
        print(end=' -> 'f'{pt}')
    elif cont == 10:
        print(end=' -> 'f'{pt}')
    pt += r
    cont += 1"""
#forma simples
print('   \033[1;7;32m+++++GERADOR DE P.A+++++\033[m')
print('=-=' * 10)
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
print('\033[1;32m(INÍCIO)\033[m', end='')
while cont <= 10:
    print(' -> 'f'\033[1;33m{pt}', end='')
    cont += 1
    pt += r
print(' \033[1;31m(FIM)\033[m')
