v = int(input('\033[1;32mDigite um número para ver a sua tabuada: \033[m'))
for c in range(1, 10+1):
    print(f'\033[1;35m{v:2} x {c} = {v*c}')


