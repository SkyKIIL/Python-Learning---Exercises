#Mesmo programa do exercicio anterior, com adicionais
Matriz = [[],[],[],[],[],[],[],[],[],[],[],[]]
#As listas de 0 a 8 são para os números principais
#A lista 9 é para os números pares
#A lista 10 é para os números da terceira coluna
P0 = int(input('\033[1mDigite um valor para a posição [0,0]: '))
Matriz[0].append(P0)
if P0 % 2 == 0:
    Matriz[9].append(P0)
P1 = int(input('Digite um valor para a posição [0,1]: '))
Matriz[1].append(P1)
if P1 % 2 == 0:
    Matriz[9].append(P1)
P2 = int(input('Digite um valor para a posição [0,2]: '))
Matriz[2].append(P2)
Matriz[10].append(P2)
if P2 % 2 == 0:
    Matriz[9].append(P2)
P3 = int(input('Digite um valor para a posição [1,0]: '))
Matriz[3].append(P3)
Matriz[11].append(P3)
if P3 % 2 == 0:
    Matriz[9].append(P3)
P4 = int(input('Digite um valor para a posição [1,1]: '))
Matriz[4].append(P4)
Matriz[11].append(P4)
if P4 % 2 == 0:
    Matriz[9].append(P4)
P5 = int(input('Digite um valor para a posição [1,2]: '))
Matriz[5].append(P5)
Matriz[10].append(P5)
Matriz[11].append(P5)
if P5 % 2 == 0:
    Matriz[9].append(P5)
P6 = int(input('Digite um valor para a posição [2,0]: '))
Matriz[6].append(P6)
if P6 % 2 == 0:
    Matriz[9].append(P6)
P7 = int(input('Digite um valor para a posição [2,1]: '))
Matriz[7].append(P7)
if P7 % 2 == 0:
    Matriz[9].append(P7)
P8 = int(input('Digite um valor para a posição [2,2]: '))
Matriz[8].append(P8)
Matriz[10].append(P8)
if P8 % 2 == 0:
    Matriz[9].append(P8)
print('-=' * 30)
print(f"""                       0 \033[1;32m{Matriz[0]} {Matriz[1]} {Matriz[2]}\033[m
                       1 \033[1;33m{Matriz[3]} {Matriz[4]} {Matriz[5]}\033[m 
                       2 \033[1;36m{Matriz[6]} {Matriz[7]} {Matriz[8]}\033[m
                          0   1   2""")
print('-=' * 30)
print(f'\033[1;32mA soma de todos os números pares: {Matriz[9]} = {sum(Matriz[9])}\033[m')
print('-=' * 30)
print(f'\033[1;31mA soma dos valores da terceira coluna: {Matriz[10]} = {sum(Matriz[10])}\033[m')
print('-=' * 30)
print(f'\033[1;34mO maior valor da segunda linha: {Matriz[11]} = {max(Matriz[11])}\033[m')