#Programa que lista uma tupla em forma tabular
#x = [i for i in range(0, 30)]
tupla = ('Pão', 1.20,
            'Carne Moída 1kg', 15.24,
            'Farinha', 2.50,
            'Arroz', 4.75,
            'Manteiga', 3.30,
            'Óleo', 6.60,
            'Feijão', 5.40,
            ' Coxinha de asa 1kg', 18.38)
print('TABELA DE PREÇOS')
print('__' * 20)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}R$ ', end='')
    elif pos % 2 == 1:
        print(f'{tupla[pos]:.2f}')
print('__' * 20)


