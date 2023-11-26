#Cálculo do IMC
peso = float(input("Digite o seu peso: "))
h = float(input('Digite sua altura em metros: '))
imc = peso / (h**2)
print('IMC: {}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
print('IMC :{}'.format(imc))