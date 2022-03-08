from time import sleep
print('\033[1;33m=-=\033[m' * 6)
print('\033[0;33mCalculador de \033[4;1mIMC!\033[m')
print('\033[1;33m=-=\033[m' * 6)
peso = float(input('\033[1;38mDigite seu peso (KG): \033[m'))
altura = float(input('\033[1;38;mDigite sua altura (m): \033[m'))
print('Calculando...')
sleep(1)
imc = peso / (altura * altura)
print('\033[1;30;43m        |TABELA  IMC|         \033[m')
print('\033[1;30;43mAbaixo de 18.5: Abaixo do peso\033[m')
print('\033[1;30;43mEntre 18.5 e 25: Peso ideal   \033[m')
print('\033[1;30;43m25 até 30: Sobrepeso          \033[m')
print('\033[1;30;43m30 até 40: Obesidade          \033[m')
print('\033[1;30;43mAcima de 40: Obesidade mórbida\033[m')
sleep(1)
if imc < 18.5:
    print(f'\033[1;33;40mSeu IMC é de {imc:.2f}m²\033[m')
    print('\033[1;33;40mVocê está abaixo do peso ideal. Se alimente mais!\033[m')
elif imc > 40:
    print(f'\033[1;31;40mSeu IMC é de {imc:.2f}m²\033[m')
    print('\033[1;31;40mVocê está com obesidade mórbida. Procure ajuda urgentemente!\033[m')
elif imc >= 30 and imc < 40:
    print(f'\033[1;31;40mSeu IMC é de {imc:.2f}m²\033[m')
    print('\033[1;31;40mVocê está com obesidade. Tome cuidado!\033[m')
elif imc >= 25 and imc < 30:
    print(f'\033[1;34;40mSeu IMC é de {imc:.2f}m²\033[m')
    print('\033[1;34;40mVocê está com sobrepeso. Comece a se cuidar!\033[m')
elif imc >= 18.5 and imc < 25:
    print(f'\033[1;32;40mSeu IMC é de {imc:.2f}m²\033[m')
    print('\033[1;32;40mVocê esta no peso ideal. Parabéns!\033[m')

