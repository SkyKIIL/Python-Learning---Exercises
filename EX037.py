num = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:\n(1) Para binário\n(2) Para octal\n(3) Para hexadecimal ')
bc = int(input('Sua opção: '))
bi = bin(num)[2:]
oc = oct(num)[2:]
he = hex(num)[2:]
if bc == 1:
    print(f'O número {num} em binário é igual a {bi}')
elif bc == 2:
    print(f'O número {num} em octal é igual a {oc}')
elif bc == 3:
    print(f'O número {num} em hexadecimal é igual a {he}')
else:
    print('Número inválido! Por favor digite um número compatível')
