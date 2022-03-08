#Contator de progressão aritmetica V3.0
print('   \033[1;7;32m+++++GERADOR DE P.A+++++\033[m')
print('=-=' * 10)
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
termo = pt
nt = 10
total = 0
print('\033[1;32m(INÍCIO)\033[m', end='')
while nt != 0:
    total += nt
    while cont <= total:
        print(f' \033[1;33m{termo}\033[m', end=' →')
        cont += 1
        termo += r
    print(' \033[1;31m(PAUSA)\033[m')
    nt = int(input('Quantos termos a mais você quer mostrar?\033[1;4m[ 0 ] para sair: \033[m'))
print(f'Você finalizou o programa com {total} termos exibidos!')
print('Obrigado por utilizar nosso programa :D!')
