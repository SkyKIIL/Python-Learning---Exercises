#Segunda tentativa do programa 089
Lista_Geral = []
#A primeira lista é para o nome, a segunda e a terceira são a nota 1 e nota 2, e a ultima é a média
while True:
    Nome = str(input('\033[1mNome do aluno: '))
    Primeira_Nota = float(input('Primeira nota: '))
    Segunda_Nota = float(input('Segunda nota: '))
    Média = (Primeira_Nota+Segunda_Nota)/2
    Lista_Geral.append([Nome, [Primeira_Nota, Segunda_Nota], Média])
    Continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if Continuar in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>9}')
print('--' * 20)
for Indice, Aluno in enumerate(Lista_Geral):
    print(f'{Indice:<4}{Aluno[0]:<10}{Média:>8.1f}')
while True:
    Ver_Nota = int(input('Quer ver a nota de que aluno? (999 para parar): '))
    if Ver_Nota == 999:
        break
        print('Finalizando...')
    elif Ver_Nota <= len(Lista_Geral) - 1:
        print(f'As notas de {Lista_Geral[Ver_Nota][0]} são: {Lista_Geral[Ver_Nota][1]}')
print('<<< OBRIGADO POR UTILIZAR >>>')
