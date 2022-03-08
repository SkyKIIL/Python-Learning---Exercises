#Programa que lê 7 números digitados pelo usuário e os separa em listas de pares e impares
Números = [[],[]]
Dados = []
for n in range(1, 8):
    Dados.append(int(input(f'{n}° valor: ')))
    if n % 2 == 0:
        Números[0].append(Dados[:])
    else:
        Números[1].append(Dados[:])
    Dados.clear()
print('-=' * 20)
print(f'Números pares : ', end='')
for Pares in Números[0]:
    print(Pares, end='_')
print(f'\nNúmeros impares: ', end='')
for Impares in Números[1]:
    print(Impares, end='_')
