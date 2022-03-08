salario = float(input('Digite o valor do seu salário: '))
n1 = salario * 1.10
n2 = salario * 1.15
if salario >= 1250.00:
    print(f'Seu aumento foi de R${n1:.2f} reais!')
else:
    print(f'Seu aumento foi de R${n2:.2f} reais!')
