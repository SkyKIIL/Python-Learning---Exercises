#Programa que lê o nome e a quantidade de partidas com a quantidade de gols feitos por partida
Jogador = {}
copia = []
Jogador['Nome'] = str(input('Nome do jogador: '))
Quantidade_Partidas = int(input(f'Número de partidas jogadas por {Jogador["Nome"]}: '))
print('-=' * 30)
for Partidas in range(0, Quantidade_Partidas):
    copia = int(input(f'Quantidade de gols na partida {Partidas}: '))
    Jogador['Gols'].append(Quantidade_Gols)
print(Jogador)