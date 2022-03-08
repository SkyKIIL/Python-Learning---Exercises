#Programa que soma os valores digitados e só encerra quando digitado 999
soma = cont = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores é {soma}!')
