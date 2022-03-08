print('\033[1;7;33m+++++VÁRIOS NÚMEROS ALEATÓRIOS+++++\033[m')
print('=-' * 18)
n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite qualquer número: '))
    if n != 999:
        cont += 1
        soma += n
print(f'Você digitou \033[1;32m{cont}\033[m números e a soma deles é \033[1;33m{soma}\033[m!')
