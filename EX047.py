print('\033[1;7;38m+++++NÚMEROS PARES ENTRE 1 E 50+++++\033[m')
print(end='\033[1;32m(INICIO)\033[m')
for c in range(2, 50, 2):
    print(end=' 'f'\033[1;33m {c}')
print(' \033[1;31m(FIM)')
