from time import sleep
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
print('Analisando...')
sleep(1)
print(f'Seus números são {num1} e {num2}')
if num1 == num2:
    print('Não existe número maior, os dois são iguais!')
elif num1 > num2:
    print(f'O primeiro valor é maior!')
elif num2 > num1:
    print(f'O segundo valor é maior!')

