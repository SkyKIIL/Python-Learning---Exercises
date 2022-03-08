#Programa que pede o nome e peso de x pessoas e os coloca em lista e mostra algumas informações
Pessoas = []
Dados = []
Maior_Peso = Menor_Peso = 0
while True:
    Dados.append(str(input('Nome: ')).capitalize())
    Dados.append(float(input('Peso: ')))
    if len(Pessoas) == 0:
        Maior_Peso = Menor_Peso = Dados[1]
    else:
        if Dados[1] > Maior_Peso:
            Maior_Peso = Dados[1]
        if Dados[1] < Menor_Peso:
            Menor_Peso = Dados[1]
    Pessoas.append(Dados[:])
    Dados.clear()
    Continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while Continuar not in 'SN':
        Continuar = str(input('Inválido! Quer continuar? [S/N]: ')).strip().upper()
    if Continuar in 'N':
        break
print(f'Seus dados: {Pessoas}')
print(f'Total de pessoas cadastradas: {len(Pessoas)}')
print(f'O maior peso foi de {Maior_Peso}Kg. Peso de: ', end='')
for p in Pessoas:
    if p[1] == Maior_Peso:
        print(f'[{p[0]}]',end=',')
print(f'\nO menor peso foi de {Menor_Peso}Kg. Peso de: ', end='')
for p in Pessoas:
    if p[1] == Menor_Peso:
        print(f'[{p[0]}]', end=',')
