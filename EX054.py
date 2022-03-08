from datetime import date
print('\033[1;7;31m+++++COMPARADOR DE MAIORIDADE+++++\033[m')
data = date.today().year
menores = 0
maiores = 0
for idade in range(1, 8):
    ids = int(input(f'\033[1;33mEm que ano a {idade}° pessoa nasceu?: \033[m'))
    if data - ids >= 21:
        maiores += 1
    else:
        menores += 1
print(f'\033[1;32mTemos um total de {maiores} pessoa(s) maiores de idade!')
print(f'\033[1;31mE também tivemos um total de {menores} pessoa(s) menores de idade!')
