print('\033[1;7;34m+++++SEQUÊNCIA DE FIBONACCI+++++\033[m')
n = int(input('Digite um número inteiro para ver sua sequência: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} {t2} ', end='')
while cont <= n:
    t3 = t1 + t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
