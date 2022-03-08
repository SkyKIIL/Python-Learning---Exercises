n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
if m >= 7:
    print(f'\033[4;7;32;40mSua nota foi {m:.2f}!\033[m')
    print('\033[4;7;32;40mVocê foi aprovado!\033[m')
elif 7 > m >= 5:
    print(f'\033[4;7;33;40mSua nota foi {m:.2f}!\033[m')
    print('\033[4;7;33;40mVocê está de recuperação!\033[m')
elif m < 5:
    print(f'\033[4;7;31;40mSua nota foi {m:.2f}!\033[m')
    print('\033[4;7;31;40mVocê foi reprovado!\033[m')
