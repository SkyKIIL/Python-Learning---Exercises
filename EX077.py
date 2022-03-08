#Programa que mostra uma tupla de palavras e suas respectivas vogais
tupla = ('Bailarina', 'Faquir', 'Popular',
         'Conta', 'Esmolas', 'Nicotina',
         'Companhia', 'Tempos', 'Longo',
         'Convexo', 'Escrita', 'Profundidade',
         'Natal', 'Sempre', 'Coluna',
         'Beleza', 'Grama', 'China',)
for listagem in tupla:
    print(f'\n\033[1;4;33mNa palavra {listagem.upper()} temos ', end=' ')
    for letras in listagem:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')

