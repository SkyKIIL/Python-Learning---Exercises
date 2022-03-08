from math import hypot
co = float(input(f'Valor do cateto oposto: '))
ca = float(input(f'Valor do cateto adjacente: '))
r = hypot(co, ca)
print(f'Cateto oposto = ({co}²)\nCateto adjacente = ({ca}²)\nHipotenusa = ({r:.2f})')