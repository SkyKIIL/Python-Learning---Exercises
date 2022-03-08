#Simulador de um caixa eletrônico
print('\033[1;31m~-' * 15)
print('\033[1;34m         CAIXA IAA')
print('\033[1;31m~-\033[m' * 15)
n50 = n20 = n10 = n1 = saque = 0
valor = int(input('Valor a ser sacado: '))
while valor != saque:
    if (valor - saque) > 50:
        n50 += 1
        saque += 50
    elif 50 > (valor - saque) >= 20:
        n20 += 1
        saque += 20
    elif 20 > (valor - saque) >= 10:
        n10 += 1
        saque += 10
    else:
        n1 += 1
        saque += 1
print(f'Seu saque foi de R${saque},00, contendo {n50 + n20 + n10 + n1} notas')
print(f'R$50,00 x {n50}')
print(f'R$20,00 x {n20}')
print(f'R$10,00 x {n10:}')
print(f'R$1,00 x {n1}')
