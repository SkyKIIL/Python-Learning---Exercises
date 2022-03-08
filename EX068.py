#Jogo de par ou ímpar utilizando o while
"""from random import randint
print('\033[1;m-=-' * 13)
print('+-+-+-+VAMOS JOGAR PAR OU ÍMPAR+-+-+-+')
print('\033[1;m-=-' * 13)
while True:
    jogador = int(input('Escolha um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    v = 0
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar?[P/I]: ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('=-' * 10 )
            print('Você VENCEU!')
            v += 1
        else:
            print('=-' * 20)
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('=-' * 20)
            print('Você VENCEU!')
            v += 1
        else:
            print('=-' * 20)
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('=-' * 20)
print(f'Você venceu {v} vezes.')"""
from random import randint
print('\033[1;32m==' * 11)
print('     PAR OU ÍMPAR')
print('==' * 11)
print('\033[m')
v = 0
while True:
    jogador = int(input('\033[mEscolha um valor: '))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    print(f'Você jogou \033[1;32m{jogador}\033[m e o computador jogou \033[1;33m{computador}.\033[m')
    print(f'Deu um total de \033[1;35m{total}\033[m pontos.')
    print('Deu \033[1;32m(PAR)\033[m' if total % 2 == 0 else 'Deu \033[1;34M(ÍMPAR)\033[M')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;32mPARABÉNS! Você venceu.\033[m')
            v += 1
        else:
            print('\033[1;31mQue pena! Você perdeu.\033[m')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('\033[1;32mPARABÉNS! Você venceu.\033[m')
            v += 1
        else:
            print('\033[1;31mQue pena! Você perdeu.\033[m')
            break
    print('Vamos jogar novamente!')
print(f'Você venceu \033[1;31m{v}\033[m vezes!')
