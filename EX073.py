#Programa que mostra os 20 primeiros colocados da tabela do Campeonato Brasileiro e mais algumas informações
times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino',
         'Corinthians', 'Fluminense', 'Cuiabá', 'Internacional', 'Atlético-GO',
         'Athletico-PR', 'Ceará-SC', 'Santos', 'Juventude', 'Bahia',
         'São Paulo', 'América-MG', 'Grêmio', 'Sport Recife', 'Chapecoense')
print('\033[1;32mTABELA DO CAMPEONATO BRASILEIRO 2021\033[m')
print(times)
print('=-' * 20)
print('\033[1;31mOS CINCO PRIMEIROS COLOCADOS DA TABELA\033[m')
print(times[0:5])
print('=-' * 20)
print('\033[1;33mOS ÚLTIMOS 4 COLOCADOS DA TABELA\033[m')
print(times[-4:])
print('=-' * 20)
print('\033[1;34mA ORDEM ALFABÉTICA DA TABELA\033[m')
print(sorted(times))
print('=-' * 20)
print('\033[1;35mPOSIÇÃO DO CHAPECOENSE NA TABELA\033[m')
print(times.index('Chapecoense')+1)
print('=-' * 20)
