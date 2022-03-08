from datetime import date
ab = int(input('Que ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ab == 0:
    ab = date.today().year
if ab % 4 == 0 and ab % 100 != 0 or ab % 400 == 0:
    print(f'O ano de {ab} é bissexto!')
else:
    print(f'O ano de {ab} não é bissexto!')
