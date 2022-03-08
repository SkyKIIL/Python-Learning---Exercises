print('\033[1;7;34m+++++PROGRESSÃO ARITMÉTICA+++++\033[m')
pt = int(input('\033[1;4mPrimeiro termo: \033[m'))
r = int(input('\033[1;4mRazão: \033[m'))
form = pt + (10 - 1) * r
print(end='\033[1;32m(Início)')
for c in range(pt, form+1, r):
    print(end=' -> 'f'\033[1;33m{c}')
print(' \033[1;31m(Fim)')
