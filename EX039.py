from datetime import date
an = int(input('Digite o seu ano de nascimento: '))
cal1 = date.today().year - an
if cal1 < 18:
    print(f'Quem nasceu em {an} tem {cal1} anos em {date.today().year}!')
    print('Você ainda irá se alistar ao serviço militar!')
    print(f'Ainda faltam {18 - cal1} ano(s) para você se alistar!')
elif cal1 == 18:
    print(f'Quem nasceu em {an} tem {cal1} anos em {date.today().year}!')
    print('Está na hora de você se alistar!')
elif cal1 > 18:
    print(f'Quem nasceu em {an} tem {cal1} anos em {date.today().year}!')
    print('Já passou da hora de você se alistar, se apresse!')
    print(f'Você deveria ter ido se alistar a {cal1 - 18} ano(s)!')


