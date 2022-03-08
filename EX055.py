print('\033[1;7;35m+++++IDENTIFICADOR DE MAIOR E MENOR PESO+++++\033[m')
maior = 0
menor = 0
for peso in range(1, 6):
    p = float(input(f'Digite o peso da {peso}° pessoa(kg): '))
    if peso == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'\033[1;31mMaior peso: {maior}kg')
print(f'\033[1;33mMenor peso: {menor}kg')

"""print('\033[1;7;35m+++++IDENTIFICADOR DE MAIOR E MENOR PESO+++++\033[m')
lst = []
for peso in range(1, 6):
    p = float(input(f'Digite o peso da {peso}° pessoa(kg): '))
    lst += [p]
print(f'Maior peso foi {max(lst)}kg')
print(f'Menor peso foi {min(lst)}kg')"""