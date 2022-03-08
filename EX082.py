#Programa que pede números aleatórios e os separa em uma lista com os numeros pares e ímpares
lista = []
par = []
impar = []
while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    if numeros % 2 == 0:
        par.append(numeros)
    elif numeros % 2 == 1:
        impar.append(numeros)
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('INVÁLIDO! Digite novamente [S/N]: ')).strip().upper()
    if cont in 'N':
        break
print('\033[1m=-\033[m' * 30)
print(f'\033[1;32mSua lista: {lista}\033[m')
print('\033[1m=-\033[m' * 30)
print(f'\033[1;31mLista só com os números pares: {par}\033[m')
print('\033[1m=-\033[m' * 30)
print(f'\033[1;36mLista só com os números ímpares: {impar}\033[m')
