print('\033[1;7;34mSOMA DE NÚMEROS.(Números ímpares são desconsiderados!)\033[m')
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('\033[1;34mDigite um valor: '))
    if (n % 2) == 0:
        soma += n
        cont += 1
print(f'\033[1;32mA soma dos {cont} número(s) PAR(ES) é {soma}')
