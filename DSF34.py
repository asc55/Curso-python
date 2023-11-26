salario = float(input('Qual o salário do funcionário: '))
print('Seu salario de R${}'.format(salario))
if salario > 1250:
    novosalario = (salario*1.10)
    print('O novo salario será de {:.2f} com 10% de aumento'.format(novosalario))
else:
    novosalario = (salario*1.15)
    print('O novo salário será de {:.2f} com 15% de aumento'.format(novosalario))