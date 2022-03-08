vcasa = float(input('Valor da casa: R$'))
sal = float(input('Valor do seu salário: '))
qanos = int(input('Em quantos anos você irá pagar a casa?: '))
pm = vcasa / (qanos * 12)
psal = sal * 0.30
if pm > psal:
    print(f'Para pagar uma casa de R${vcasa} em {qanos} anos a prestação será de R${pm:.2f}')
    print('Seu empréstimo foi NEGADO!')
elif pm < psal:
    print(f'Para pagar uma casa de R${vcasa} em {qanos} anos a prestação será de R${pm:.2f}')
    print('Seu empréstimo foi concebido!')

