#Programa que lê os dados de uma pessoa e coloca em um dicionario
import sys
from datetime import date
#sys.exit() para finalizar o programa quando quiser
Pessoa = {}
Pessoa['Nome'] = str(input('Nome: '))
Pessoa['Idade'] = int(input('Ano de nascimento: '))
Pessoa['Carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if Pessoa['Carteira de trabalho'] == 0:
    print('-=' * 30)
    print(f"""Seu nome: {Pessoa['Nome']}.
Sua idade: {date.today().year - Pessoa['Idade']} anos.
Seu CPTS: {Pessoa['Carteira de trabalho']}.""")
    sys.exit()
Pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
Pessoa['Aposentadoria'] = Contador_Aposentadoria
Pessoa['Salário'] = float(input('Salário: '))
print('-=' * 30)
print(f"""Seu nome: {Pessoa['Nome']}
Sua idade: {date.today().year - Pessoa['Idade']}
Seu CPTS: {Pessoa['Carteira de trabalho']}
Ano de contratação: {Pessoa['Ano de contratação']}
Salário: R${Pessoa['Salário']}
Aposentadoria: 65 - idade       """)

