print('\033[1;32m=' * 30)
print('\033[1;31m  *IDENTIFICADOR COMPLETO*')
print('\033[1;32m=\033[m' * 30)
#CONTADORES
media = 0
nomeH = 0
idadeH = 0
idadeMF = 0
for inf in range(1,5):
    print(f'\033[1;32m====={inf}°PESSOA=====\033[m')
    n = str(input('Nome: ')).strip().upper()
    i = int(input('Idade: '))
    s = str(input('Sexo[M/F]: ')).strip().upper()
    media += i / 4
    if inf == 1 and s in "M":
        idadeH = i
        nomeH = n
    if s in "M" and i > idadeH:
        idadeH = i
        nomeH = n
    if s in "F" and i < 20:
        idadeMF += 1
print(f'\033[1;32mA média das idades é {media} anos!')
print(f'\033[1;34mO nome do homem mais velho é {nomeH} e sua idade é {idadeH} anos!')
print(f'\033[1;35mAo todo são {idadeMF} mulher(es) com menos de 20 anos!')
#Metodo alternativo
"""print('\033[1;32m=' * 30)
print('\033[1;31m  *IDENTIFICADOR COMPLETO*')
print('\033[1;32m=\033[m' * 30)
media = 0
lista_nome = []
lista_nome_h = []
lista_idade = []
lista_sexo = []
lista_idade_h = []
lista_idade_m = []
for ic in range(1,5):
    print(f'\033[1;31m----- {ic}° PESSOA -----')
    nome = str(input('\033[1;32mNome: ')).strip().upper()
    lista_nome.append(nome)
    idade = int(input('\033[1;32mIdade: '))
    lista_idade.append(idade)
    sexo = str(input('\033[1;32mSexo[M/F]: ')).strip().upper()
    lista_sexo.append(sexo)
    media += idade / 4
    if sexo == "M":
        lista_nome_h.append(nome)
        lista_idade_h.append(idade)
    if sexo == "F" and idade < 20:
        lista_idade_m.append(idade)
print(f'\033[1;7;35mMédia das idades: {media} anos!\033[m')
print(f'Nome do homem mais velho: {lista_nome_h[lista_idade_h.index(max(lista_idade_h))]}')
print(f'O total de mulheres abaixo de 20 anos: {len(lista_idade_m)}')"""
