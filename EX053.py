print('\033[1;7;35m+++++DETECTOR DE PALÍNDROMO+++++\033[m')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
resol = ''.join(palavras)
for c in range(1):
    if resol == resol[::-1]:
        print(f'O inverso de \033[1;4;32m{resol}\033[m é \033[1;4;32m{resol[::-1]}')
        print('\033[1;32mA frase digitada É UM PALÍNDROMO')
    else:
        print(f'O inverso de \033[1;4;31m{resol}\033[m é \033[1;4;31m{resol[::-1]}')
        print('\033[1;31mA frase digitada NÃO É UM PALÍNDROMO')
