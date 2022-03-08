nome = str(input('Digite seu nome completo: ')).strip()
lM = nome.upper()
lm = nome.lower()
ql = len(nome) - nome.count(' ')
pn = nome.find(' ')
print(f'Maiúsculas: {lM}\nMinúsculas: {lm}\nQuantidade de letras: {ql}\nO primeiro nome possui: {pn} letras')

