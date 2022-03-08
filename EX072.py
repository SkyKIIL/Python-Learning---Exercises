#Programa que mostra um número entre 0 e 20 por extenso
listnum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'cartorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    print(f'\033[1;32mVocê digitou o número \033[1;4m{listnum[numero]}!\033[m')
    cont = str(input('Você quer continuar? [S/N]: ')).strip().upper()
    if cont == 'N':
        break
    while cont not in 'SN':
        cont = str(input('Digite novamente! [S/N]: ')).strip().upper()
print('Obrigado por utilizar :)')


