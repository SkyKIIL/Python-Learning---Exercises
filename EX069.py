#Programa que cadastra o nome, idade e sexo de uma pessoa
cont = sexo = mais18 = Hcadastrado = Mmenos20 = continuar = 0
while continuar != 'N':
    print('\033[1;33m=\033[m' * 29)
    print('\033[1;32m    CADASTRO DE PESSOAS\033[m')
    print('\033[1;33m=\033[m' * 29)
    idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        Hcadastrado += 1
    if idade < 20 and sexo == 'F':
        Mmenos20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
print('\033[1;33m=\033[m' * 29)
print(f'{mais18} pessoa(s) com mais de 18 foram cadastradas!')
print(f'{Hcadastrado} homem(s) foram cadastrados!')
print(f'{Mmenos20} mulher(es) tem menos de 18!')
print('\033[1;33m=\033[m' * 29)
print('Obrigado por utilizar :)')
