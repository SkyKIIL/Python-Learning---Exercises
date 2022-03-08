#Programa que gera 4 números aleatórios para cada jogador e mostra os em ordem
from random import randint
from time import sleep
Lista_De_Jogadores = []
Lugar = [1, 2, 3, 4]
Jogadores = {'Jogador_1': f'{randint(1, 6)}',
                      'Jogador_2': f'{randint(1, 6)}',
                      'Jogador_3': f'{randint(1, 6)}',
                      'Jogador_4': f'{randint(1, 6)}'}
Lista_De_Jogadores.append(Jogadores.copy())
print('Valores sorteados: ')
for I in Lista_De_Jogadores:
    for Jogador, Valor in I.items():
        print(f'    {Jogador}: {Valor} ')
        sleep(0.5)
print('Ranking dos jogadores: ')
for item in sorted(Jogadores, key= Jogadores.get, reverse=True):
    print(f'    {(sample(range(4)), 1)}° lugar: {item} com  ')
