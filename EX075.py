#Programa que lê 4 numeros pelo teclado e mostra algumas informações
num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite novamente outro valor: ')),
       int(input('Digite o último valor: ')))
print(f'\033[1;32mVocê digitou os valores: {num}\033[m')
print(f'\033[1;35mO número nove apareceu {num.count(9)} vez(es)!\033[m')
if 3 in num:
    print(f'\033[1;34mO número 3 aparece na {num.index(3)+1}° posição\033[m')
else:
    print('\033[1;31mO número 3 não aparece nenhuma vez!\033[m')
print(f'\033[1;33mOs números pares foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
