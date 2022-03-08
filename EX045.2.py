#SEGUNDA TENTATIVA DO JOKENPO
from time import sleep
from random import randint
#Lista de escolha aleatória do computador
computador = randint(0, 2)
itens = ('Pedra', 'Tesoura', 'Papel')
print('\033[1;31m+++++++Bem-vindo ao jokenpô robótico+++++++')
#Regras
print('\033[1;7;35;40mVou te dizer as regras:            \033[m')
print('\033[1;4;7;35;40m[ 0 ]PEDRA ganha da tesoura.            \033[m')
print('\033[1;4;7;35;40m[ 1 ]TESOURA ganha do papel.            \033[m')
print('\033[1;4;7;35;40m[ 2 ]PAPEL ganha da pedra.              \033[m')
print('\033[1;7;35mIrei escolher umas das três opções!\033[m')
sleep(1)
print('\033[1;31mEscolhendo...')
sleep(2)
#Usuário escolhe uma opção
usuario = int(input('\033[1;31mPronto! Qual sua jogada?: '))
print('\033[1;33mJO')
sleep(1)
print('\033[1;33mKEN')
sleep(1)
print('\033[1;33mPO!!!')
sleep(1)
print('*-*' * 10)
print(f'COMPUTADOR jogou {itens[computador]}')
print(f'JOGADOR jogou {itens[usuario]}')
print('*-*' * 10)
#Pedra ganhando da tesoura
if computador == 0:
    if usuario == 0:
        print('\033[1;7;33mOlha só, deu empate!\033[m') #Empate
    elif usuario == 1:
        print('\033[1;7;31mHAHA! Você perdeu!\033[m') #Computador vence
    elif usuario == 2:
        print('\033[1;7;32mNÃAOO! Você ganhou!\033[m') #Usuario vence
    else:
        print('\033[1;7;30;40mOpção INVÁLIDA! Tente novamente.\033[m')
if computador == 1:
    if usuario == 0:
        print('\033[1;7;32mNÃAOO! Você ganhou!\033[m') #Usuario vence
    elif usuario == 1:
        print('\033[1;7;33mOlha só, deu empate!\033[m') #Empate
    elif usuario == 2:
        print('\033[1;7;31mHAHA! Você perdeu!\033[m') #Computador vence
    else:
        print('\033[1;7;30;40mOpção INVÁLIDA! Tente novamente.\033[m')
if computador == 2:
    if usuario == 0:
        print('\033[1;7;31mHAHA! Você perdeu!\033[m') #Computador vence
    elif usuario == 1:
        print('\033[1;7;32mNÃAOO! Você ganhou!\033[m') #Usuario vence
    elif usuario == 2:
        print('\033[1;7;33mOlha só, deu empate!\033[m') #Empate
    else:
        print('\033[1;7;30;40mOpção INVÁLIDA! Tente novamente.\033[m')
