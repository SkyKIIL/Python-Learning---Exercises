from time import sleep
viagem = float(input('Qual a distância da sua viagem?: '))
print('Processando...')
sleep(1)
print(f'Você está prestes a começar uma viagem de {viagem}KM!')
if viagem <= 200:
    print(f'Você pagará R${viagem *0.50} reais pela viagem!')
else:
    print(f'Você pagará R${viagem *0.45} reais pela viagem!')

