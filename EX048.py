print('\033[1;7;34m+++++SOMA DOS NÚMEROS ÍMPARES MÚLTIPLOS DE 3 DE 1 ATÉ 500+++++\033[m')
print('\033[1;32m(INICIO)\033[m')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'\033[1;4mA soma dos {cont} valores é {soma}\033[m!')
print('\033[1;31m(FIM)')
