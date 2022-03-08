n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
if n2 < n1 > n3:
    print(f'Maior número: {n1}')
if n1 < n2 > n3:
    print(f'Maior número: {n2}')
if n1 < n3 > n2:
    print(f'Maior número: {n3}')
if n2 > n1 < n3:
    print(f'Menor número: {n1}')
if n1 > n2 < n3:
    print(f'Menor número: {n2}')
if n1 > n3 < n2:
    print(f'Menor número: {n3}')

