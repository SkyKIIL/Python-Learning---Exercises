#Programa que pede varios numeros aleatorios e os adiciona em uma lista
lista = []
repetido = 0
while True:
    numeros = int(input('Digite um valor: '))
    if numeros not in lista:
        lista.append(numeros)
        print('Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado! Não foi possível adicionar. ')
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('INVÁLIDO! Digite novamente [S/N]: ')).strip().upper()
    if cont in 'N':
        break
print(f'Você digitou os valores: {sorted(lista)}')
