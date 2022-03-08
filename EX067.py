#Programa que mostra a tabuada de um número escolhido
from time import sleep
print('\033[1;7;32m+++++TABUADA+++++\033[m')
while True:
    print('\033[1;32m=-=\033[m' * 10)
    tabu = int(input('Digite um número para ver sua tabuada: '))
    print('\033[1;32m=-=\033[m' * 10)
    if tabu < 0:
        break
    for c in range(0, 11):
        print(f'{tabu} x {c} = {tabu * c}')
print('Finalizando...')
sleep(1)
print('Fim do programa :)')