#Programa que conta quantos números foram digitados, tira a média deles e mostra o maior e menor número
print('\033[1;7;37m+++++LEITOR DE NÚMEROS ALEATÓRIOS+++++\033[m')
n = cont = soma = ctnr = maior = menor = 0
while ctnr != 'N':
    n = int(input('Digite um número: '))
    ctnr = str(input('Quer continuar?[S/N]: ')).strip().upper()
    cont += 1
    soma += n
    m = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Você digitou {cont} números!')
print(f'A média de todos os valores é {n}!')
print(f'O maior número é {maior} e o menor é {menor}!')
