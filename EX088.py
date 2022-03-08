#Programa que pede a quantidade de jogos que vai ser feito na mega sena e gera números
from random import sample
from time import sleep
Lista_De_Jogos = []
print('\033[1m-------------------------------')
print('      JOGA NA MEGA SENA')
print('-------------------------------')
Quantidade_De_Jogos = int(input('Quantos jogos serão feitos? '))
if Quantidade_De_Jogos == 1:
    print(f'=====> SORTEANDO {Quantidade_De_Jogos} JOGO <======')
else:
    print(f'=====> SORTEANDO {Quantidade_De_Jogos} JOGOS <======')
for c in range(0, Quantidade_De_Jogos):
    Numeros = (sample(range(60), 6))
    Lista_De_Jogos.append(Numeros)
    Lista_De_Jogos[c].sort()
    print(f'Jogo {c+1}: {Lista_De_Jogos[c]}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-\033[m')

