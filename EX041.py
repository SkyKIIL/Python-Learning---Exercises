from time import sleep
from datetime import date
an = int(input('\033[7;37;40mSua data de aniversário: \033[m'))
ctgr = date.today().year - an
print('Calculando...')
sleep(1)
if ctgr <= 9:
    print(f'\033[4;37;40mO atleta tem {ctgr} anos!\033[m\n\033[4;37;40mSua classificação: MIRIM!\033[m')
elif ctgr <= 14:
    print(f'\033[4;35;40mO atleta tem {ctgr} anos!\033[m\n\033[4;35;40mSua classificação: INFANTIL!\033[m')
elif ctgr <= 19:
    print(f'\033[4;32;40mO atleta tem {ctgr} anos!\033[m\n\033[4;32;40mSua classificação: JUNIOR!\033[m')
elif ctgr <= 25:
    print(f'\033[4;31;40mO atleta tem {ctgr} anos!\033[m\n\033[4;31;40mSua classificação: SÊNIOR!\033[m')
else:
    print(f'\033[4;36;40mO atleta tem {ctgr} anos!\033[m\n\033[4;36;40mSua classificação: MASTER!\033[m')

