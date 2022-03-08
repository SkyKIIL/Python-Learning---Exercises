#Simulador de um caixa eletrônico
print('\033[1;31m~-' * 15)
print('\033[1;34m         CAIXA ITAU')
print('\033[1;31m~-\033[m' * 15)
valor = int(input('Valor que deseja sacar: '))
total = valor
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\033[1;36mTotal de {totced} cédula(s) de R${ced}\033[m')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Obrigado por utilizar nosso programa :)')
