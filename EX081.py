#Programa que pede números aleatorios e mostra algumas informações
numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('INVÁLIDO! Digite novamente [S/N]: ')).strip().upper()
    if continuar in 'N':
        break
print('\033[1m=-\033[m' * 20)
print(f'Foram digitados {len(numeros)} elementos!')
decres = sorted(numeros, reverse=True)
print(f'Valores em ordem decrescente: {decres}')
if 5 not in numeros:
    print('O valor 5 não foi digitado!')
else:
    print('O valor 5 faz parte da lista! ')
