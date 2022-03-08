#MÉTODO QUE FIZ, COM MAIS LINHAS SÓ QUE ORGANIZADO TAMBÉM.
"""print('\033[1;7;33m+++++REGISTRO DE SEXO+++++\033[m')
s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while s != 'F' and s != 'M':
    if s != 'F' and s != 'M':
        s = str(input('\033[1;31mDados inválidos. Por favor, informe seu sexo: \033[m')).strip().upper()
masc = s.replace('M', 'Masculino')
femi = s.replace('F', 'Feminino')
if s == 'M':
    print(f'\033[1;34mSexo {masc} registrado com sucesso!')
if s == 'F':
    print(f'\033[1;35mSexo {femi} registrado com sucesso!')"""
#MÉTODO SIMPLES
print('\033[1;7;33m+++++REGISTRO DE SEXO+++++\033[m')
sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in "FfMm":
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')