#Programa que cria uma matriz de acordo com os valores digitados
Matriz = [[],[],[],[],[],[],[],[],[]]
P0 = int(input('\033[1mDigite um valor para a posição [0,0]: '))
Matriz[0].append(P0)
P1 = int(input('Digite um valor para a posição [0,1]: '))
Matriz[1].append(P1)
P2 = int(input('Digite um valor para a posição [0,2]: '))
Matriz[2].append(P2)
P3 = int(input('Digite um valor para a posição [1,0]: '))
Matriz[3].append(P3)
P4 = int(input('Digite um valor para a posição [1,1]: '))
Matriz[4].append(P4)
P5 = int(input('Digite um valor para a posição [1,2]: '))
Matriz[5].append(P5)
P6 = int(input('Digite um valor para a posição [2,0]: '))
Matriz[6].append(P6)
P7 = int(input('Digite um valor para a posição [2,1]: '))
Matriz[7].append(P7)
P8 = int(input('Digite um valor para a posição [2,2]: '))
Matriz[8].append(P8)
print('-=' * 30)
print(f"""                       0 \033[1;32m{Matriz[0]} {Matriz[1]} {Matriz[2]}\033[m
                       1 \033[1;33m{Matriz[3]} {Matriz[4]} {Matriz[5]}\033[m 
                       2 \033[1;36m{Matriz[6]} {Matriz[7]} {Matriz[8]}\033[m
                          0   1   2""")
#Segunda resolução
Matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        Matriz2[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{Matriz2[l][c]:^5}]', end='')
    print()