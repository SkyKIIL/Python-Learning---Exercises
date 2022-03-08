#Programa que lê 5 valores e os guarda em uma lista e mostra o maior, o menor e sua posição
#lista = [i for i in range(0, 30) if i % 2 == 0]
#print(lista)
lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'\033[1;34mVocê digitou os valores {lista}\033[m')
print('~~' * 20)
print(f'\033[1;32mO maior valor da lista foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}', end='...')
print()
print(f'\033[1;31mO menor valor da lista foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}', end='...')
