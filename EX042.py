#Primeira tentativa
from time import sleep
from termcolor import colored
print(colored('=-=', 'blue') * 22)
print(colored('Digite 3 números para verificar se é possível formar um triângulo!', 'yellow'))
print(colored('=-=', 'blue') * 22)
sleep(1)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
print(colored('Calculando...', 'cyan'))
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 == r3:
    print(colored('Os segmentos acima PODEM formar um triângulo!', 'green'))
    print('Será formado um triângulo Equilátero!')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 == r3 or r1 == r2 != r3:
    print(colored('Os segmentos acima PODEM formar um triângulo!', 'green'))
    print('Será formado um triângulo Isósceles!')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 != r3:
    print(colored('Os segmentos acima PODEM formar um triângulo!', 'green'))
    print('Será formado um triângulo Escaleno!')
else:
    print(colored('Os segmentos acima NÃO PODEM formar um triângulo!', 'red'))

#Segunda tentativa
print(colored('=-=', 'blue') * 22)
print(colored('Digite 3 números para verificar se é possível formar um triângulo!', 'yellow'))
print(colored('=-=', 'blue') * 22)
sleep(1)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
print(colored('Calculando...', 'cyan'))
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print(colored('Os segmentos acima PODEM formar um triângulo!', 'green'))
        print('Será formado um triângulo Equilátero!')
    elif r1 != r2 != r3 != r1:
        print(colored('Os segmentos acima PODEM formar um triângulo!', 'green'))
        print('Será formado um triângulo Escaleno!')
    else:
        print(colored('Os segmentos acima PODEM formar um triângulo!', 'green'))
        print('Será formado um triângulo Isósceles!')
else:
    print(colored('Os segmentos acima NÃO PODEM formar um triângulo!', 'red'))