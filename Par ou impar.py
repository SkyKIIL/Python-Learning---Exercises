#Programa que determina se um número é par ou impar
import sys

"""while True:
    NUMERO = int(input('Digite um número: (00 para sair)'))
    if NUMERO == 00:
        sys.exit()
    if NUMERO % 2 == 0:
        print('Seu número é par!')
    else:
        print('Seu número é impar!')"""
while True:
    try:
        numero = int(input('Digite um número: '))
        if numero % 2 == 0:
            print('Número par!')
        else:
            print('Número impar!')
    except:
        print('Digite apenas números!')