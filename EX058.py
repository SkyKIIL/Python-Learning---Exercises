#PRIMEIRA TENTATIVA
from random import choice, randint
from time import sleep
print('\033[1;34m=-=' * 20)
print('\033[1;32m        ++++++++++++JOGO DA ADIVINHAÇÃO++++++++++++')
print('\033[1;34m=-=' * 20)
comp = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
comps = randint(0, 10)
sleep(0.5)
print('\033[1;31m[COMPUTADOR]:')
print('Vou pensar em um número de 0 à 10!')
print('.')
sleep(0.5)
print('..')
sleep(0.5)
print('...')
print('ADIVINHE!')
usu = int(input('[COMPUTADOR] Que número eu escolhi?: \033[M'))
print('Analisando...')
sleep(0.5)
tent = 1
while usu != comp:
    if usu == comp:
        print(f'\033[1;35m[COMPUTADOR]: PARABÉNS! Você ganhou depois de {tent} tentativa(s)!')
        print(f'\033[1;4m[COMPUTADOR] = ({comp}) / [USUÁRIO] = ({usu})')
    if usu != comp:
        tent += 1
        print(f'\033[1;31m[COMPUTADOR]: RESPOSTA ERRADA!')
        usu = int(input('\033[1;32m[COMPUTADOR]: Tente novamente: \033[m'))
print(f'\033[1;35m[COMPUTADOR]: PARABÉNS! Você ganhou depois de {tent} tentativa(s)!')
print(f'\033[1;4m[COMPUTADOR] = ({comp}) / [USUÁRIO] = ({usu})')
