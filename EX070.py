#Simulador de um mercado com produto e valor
total = maismil = continuar = preco = menor = cont = 0
barato = ' '
print('\033[1;34m<>\033[m' * 10)
print('   MERCADO ALVES')
print('\033[1;34m<>\033[m' * 10)
while continuar != 'N':
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = int(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maismil += 1
    continuar = ' '
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()
        if continuar == 'N':
            break
    print('=' * 23)
print(f'O total gasto na compra foi de R${total} reais !')
print(f'{maismil} produto(s) custam mais de mil reais ! ')
print(f'O produto mais barato foi {barato} e custa {menor} !')

