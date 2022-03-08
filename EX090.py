#Programa que lê o nome e a média de um aluno e mostra sua situação
Aluno = {}
Situação = {'SituaçãoA': 'Aprovado', 'SituaçãoB': 'Reprovado'}
Lista = []
Aluno['Nome'] = str(input('Nome do aluno: '))
Aluno['Média'] = float(input('Média do aluno: '))
Lista.append(Aluno.copy())
print('-=' * 30)
if Lista[0]['Média'] < 7:
    print(f'Nome do aluno: {Lista[0]["Nome"]}')
    print(f'Sua média: {Lista[0]["Média"]}')
    print(f'Situação é igual a {Situação["SituaçãoB"]}')
else:
    print(f'Nome do aluno: {Lista[0]["Nome"]}')
    print(f'Sua média: {Lista[0]["Média"]}')
    print(f'Situação é igual a {Situação["SituaçãoA"]}')