#PRIMEIRA TENTATIVA DO JOKENPO
from time import sleep
from random import choice
#Lista de escolha aleatória do computador
lista = choice(['Tesoura', 'Papel', 'Pedra'])
ls = lista
print('\033[1;31m+++++++Bem-vindo ao jokenpô robótico+++++++')
#Regras
print('\033[1;7;36;40mVou te dizer as regras:            \033[m')
print('\033[1;4;7;36;40mPEDRA ganha da tesoura.            \033[m')
print('\033[1;4;7;36;40mTESOURA ganha do papel.            \033[m')
print('\033[1;4;7;36;40mPAPEL ganha da pedra.              \033[m')
print('\033[1;7;36mIrei escolher umas das três opções!\033[m')
sleep(1)
print('\033[1;31mEscolhendo...')
sleep(2)
#Usuário escolhe uma opção
op = str(input('\033[1;31mPronto! Qual sua jogada?: ')).capitalize()
print('\033[1;33mJO')
sleep(1)
print('\033[1;33mKEN')
sleep(1)
print('\033[1;33mPO!!!')
sleep(1)
if op == ls:
    print('Olha só, deu empate!')
    print(f'Eu escolhi {ls} e você {op}!')
#Pedra ganhando da tesoura
elif op == 'Pedra' and ls == 'Tesoura':
    print('\033[1;32mNÃAOO! Você ganhou!')
    print(f'Eu escolhi {ls} e você {op}!')
elif ls == 'Pedra' and op == 'Tesoura':
    print('\033[1;31mHAHA! Eu ganhei!')
    print(f'Eu escolhi {ls} e você {op}!')
elif op == 'Pedra' and ls == 'Papel':
    print('\033[1;32mNÃAOO! Você ganhou!')
    print(f'Eu escolhi {ls} e você {op}!')
elif ls == 'Pedra' and op == 'Papel':
    print('\033[1;31mHAHA! Eu ganhei!')
    print(f'Eu escolhi {ls} e você {op}!')
#Tesoura ganhando do papel
elif op == 'Tesoura' and ls == 'Papel':
    print('\033[1;32mNÃAOO! Você ganhou!')
    print(f'Eu escolhi {ls} e você {op}!')
elif ls == 'Tesoura' and op == 'Papel':
    print('\033[1;31mHAHA! Eu ganhei!')
    print(f'Eu escolhi {ls} e você {op}!')
elif op == 'Tesoura' and ls == 'Pedra':
    print('\033[1;32mNÃAOO! Você ganhou!')
    print(f'Eu escolhi {ls} e você {op}!')
elif ls == 'Tesoura' and op == 'Pedra':
    print('\033[1;31mHAHA! Eu ganhei!')
    print(f'Eu escolhi {ls} e você {op}!')
#Papel ganhando da pedra
elif op == 'Papel' and ls == 'Pedra':
    print('\033[1;32mNÃAOO! Você ganhou!')
    print(f'Eu escolhi {ls} e você {op}!')
elif ls == 'Papel' and ls == 'Pedra':
    print('\033[1;31mHAHA! Eu ganhei!')
    print(f'Eu escolhi {ls} e você {op}!')
elif op == 'Papel' and ls == 'Tesoura':
    print('\033[1;32mNÃAOO! Você ganhou!')
    print(f'Eu escolhi {ls} e você {op}!')
elif ls == 'Papel' and ls == 'Tesoura':
    print('\033[1;31mHAHA! Eu ganhei!')
    print(f'Eu escolhi {ls} e você {op}!')
else:
    print('\033[1;31mEscolha uma opção VÁLIDA!')
