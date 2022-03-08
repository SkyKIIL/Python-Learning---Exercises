frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print(f'A letra A aparece {frase.find("A")} vezes na frase')
print(f'A primeira letra A aparece na posição {frase.find("A")+1}')
print(f'A ultima letra A aparece na posição {frase.rfind("A")+1}')




