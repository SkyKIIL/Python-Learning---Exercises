#n = str(input('Digite um número entre 0 e 9999: '))
#n1 = n[3:4]
#n2 = n[2:3]
#n3 = n[1:2]
#n4 = n[0:1]
#print(f'Unidade: ({n1})\nDezena:  ({n2})\nCentena: ({n3})\nMilhar:  ({n4})')

num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
u2 = num // 10 % 10
u3 = num // 100 % 10
u4 = num // 1000 % 10
print(f'Unidade: {u}\nDezena: {u2}\nCentena: {u3}\nMilhar: {u4}')



