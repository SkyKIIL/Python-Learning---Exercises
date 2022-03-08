#Programa que pede para o usuário digitar uma expressão qualquer entre parênteses
#para verificar se ela está correta
Parenteses = []
Expressão = str(input('Digite uma expressão matemática: '))
for Exp in Expressão:
    if '(' in Exp:
        Parenteses.append(Exp)
    elif ')' in Exp:
        if '(' in Parenteses:
            Parenteses.pop()
        else:
            Parenteses.append(Exp)
if len(Parenteses) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')

