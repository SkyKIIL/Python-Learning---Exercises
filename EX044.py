from time import sleep
print('\033[1;32m=======Redes Alves=======')
pn = float(input('\033[1;33mValor das compras: R$'))
print('\033[1;7;33;40m           |FORMAS DE PAGAMENTO|                    \033[m')
print('\033[1;7;33;40m[ 1 ]À vista no dinheiro ou cheque: 10% de desconto \033[m')
print('\033[1;7;33;40m[ 2 ]À vista no cartão: 5% de desconto              \033[m')
print('\033[1;7;33;40m[ 3 ]2x no cartão: preço normal                     \033[m')
print('\033[1;7;33;40m[ 4 ]3x ou mais no cartão: 20% de juros             \033[m')
print('\033[1;7;33;40mOBS: Digite o número referente a forma de pagamento!\033[m')
print('\033[1;33mAnalisando...')
sleep(1)
cp = int(input('\033[1;33mForma de pagamento: '))
dd = pn * 0.90
cd = pn * 0.95
cj = pn * 1.20
if cp == 1:
    print('Calculando...')
    sleep(1)
    print(f'Sua forma de pagamento é no dinheiro/cheque!')
    print(f'De R${pn:.2f} passará a custar R${dd:.2f} com 10% de desconto!')
elif cp == 2:
    print('Calculando...')
    sleep(1)
    print('Sua forma de pagamento é no cartão à vista!')
    print(f'De R${pn:.2f} passará a custar R${cd:.2f} com 5% de desconto!')
elif cp == 3:
    print('Calculando...')
    sleep(1)
    print('Sua forma de pagamento é no cartão em 2x sem juros!')
    print(f'Não haverá alteração no preço das compras, que custam R${pn}!')
    print(f'Você pagará 2 parcelas de R${pn / 2}!')
elif cp == 4:
    p = int(input('Quantas parcelas?: '))
    print('Calculando...')
    sleep(1)
    print(f'Sua forma de pagamento é no cartão em {p}x!')
    print(f'Suas compras de R${pn} passarão a custar R${cj} com 20% de juros!')
    print(f'Você pagará {p} parcelas de R${(pn / p) * 1.20:.2f}!')
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
    print(f'Suas compras de R${pn} passará a custar R${pn}!')
