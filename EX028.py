from random import choice, randint
from time import sleep
import playsound
from termcolor import colored
#r = randint(0, 5)
lista = [0, 1, 2, 3, 4, 5]
w = choice(lista)
while True:
    print(colored('-=-', 'yellow') * 19)
    print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
    print(colored('-=-', 'yellow') * 19)
    sleep(1)
    n = int(input('Que número eu pensei? '))
    print(colored('Processando...', 'cyan'))
    sleep(1)
    if n >= 6:
        print(colored('Eu mandei você pensar em um número de 1 à 5, tente de novo!.', 'magenta'))
        playsound.playsound('uuepa.mp3')

    if n == w:
        print(colored('Você ganhou , parabéns!', 'green'))
        playsound.playsound('rapaaaz.mp3')

    else:
        print(colored(f'EU GANHEI! Pois pensei no {w} e não no {n}!', 'red'))
        playsound.playsound('cavaloo.mp3')




