#Programa que analisa o nome e duas notas de x alunos e mostra média e notas individuais de cada
Lista_Total = []
Lista_Individual = []
dados = []
dados2 = []
Mostrar_Nota = Contagem = 0
while True:
    Nome_Do_Aluno = str(input('Nome do aluno: ')).strip().capitalize()
    Primeira_Nota = float(input('Primeira nota: '))
    Segunda_Nota = float(input('Segunda nota: '))
    Media = (Primeira_Nota + Segunda_Nota) / 2
    dados.append(Nome_Do_Aluno)
    dados.append(Media)
    Lista_Total.append(dados[:])
    Contagem += 1
    dados.clear()
    dados2.append(Nome_Do_Aluno)
    dados2.append(Primeira_Nota)
    dados2.append(Segunda_Nota)
    Lista_Individual.append(dados2[:])
    dados2.clear()
    Continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if 'N' in Continuar:
        print('\033[1m-=\033[m' * 30)
        for lista in Lista_Total:
            for c in range(0, Contagem):
                print(f'{c} {lista}')
        while Mostrar_Nota != 999:
            Mostrar_Nota = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
            if Mostrar_Nota != 999:
                print(f'{Lista_Individual[Mostrar_Nota]}')
    if Mostrar_Nota == 999:
        break
