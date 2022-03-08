#Programa que gera números aleatórios e coloca em tuplas
from random import randint
print('\033[1;31mGERADOR DE NÚMEROS ALEATÓRIOS\033[m')
numero1 = randint(0, 9)
numero2 = randint(0, 9)
numero3 = randint(0, 9)
numero4 = randint(0, 9)
numero5 = randint(0, 9)
soma = numero1, numero2, numero3, numero4, numero5
print(f'Os valores gerados foram: {soma}')
print(f'O maior valor foi {max(soma)}')
print(f'O menor valor foi {min(soma)}')
