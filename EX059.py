from time import sleep
print('\033[1;7;34m+++++MENU DE OPÇÕES+++++\033[m')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
print('\033[1;32m+++++TABELA DE OPÇÕES+++++')
print('\033[1;33m[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\033[m')
resposta = int(input('>>>>> Qual é a sua opção? '))
while resposta != 5:
    if resposta == 1:
        print(f'A soma de {n1:.1f} e {n2:.1f} é {n1 + n2:.1f}!')
        print('==-' * 10)
        print('\033[1;33m[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\033[m')
        resposta = int(input('>>>>> Qual é a sua opção? '))
    elif resposta == 2:
        print(f'A multiplicação de {n1:.1f} e {n2:.1f} é {n1 * n2:.1f}!')
        print('==-' * 10)
        print('\033[1;33m[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\033[m')
        resposta = int(input('>>>>> Qual é a sua opção? '))
    elif resposta == 3:
        print(f'O maior número é {max(n1, n2)}!')
        print('==-' * 10)
        print('\033[1;33m[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\033[m')
        resposta = int(input('>>>>> Qual é a sua opção? '))
    elif resposta == 4:
        print('+++Digite abaixo os novos números+++')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        print('==-' * 10)
        print('\033[1;33m[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\033[m')
        resposta = int(input('>>>>> Qual é a sua opção? '))
    else:
        print('Opção INVÁLIDA! Tente novamente.')
        resposta = int(input('>>>>> Qual é a sua opção? '))
print('Finalizando...')
sleep(1)
print('\033[1;32mObrigado por utilizar nosso programa :)')
