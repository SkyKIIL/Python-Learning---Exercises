from math import factorial
#Com WHILE.
"""print('+++++FATORIAL+++++')
n = int(input('Digite um número para ver seu fatorial: '))
c = n
f = 1
print(end=f'Calculando {n}!')
while c > 0:
    print(end=' 'f'{c}')
    print(end=' x' if c > 1 else ' ')
    f *= c
    c -= 1
print(f'\nFatorial de {n} é {f}!')"""
#Com FOR.
print('+++++FATORIAL+++++')
n = int(input('Digite um número para ver seu fatorial: '))
f = 1
print(f'Calculando {n}! = ', end='')
for n in range(n, 0, -1):
    print(f'{n}', end=' ')
    print('x ' if n > 1 else '= ', end='')
    f *= n
print(f'{f}!')
#Com a biblioteca MATH usando o factorial.
"""print('+++++FATORIAL+++++')
n = int(input('Digite um número para ver seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n}! é {f}!')"""
