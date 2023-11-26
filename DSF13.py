salario = float(input('Qual o salário do funcionário: R$'))
#novosalario = (salario*1.15)
aumento = (salario*15)/100
novosalario = salario + aumento
print('Após o aumento, o salário que antes era de R${:.2f}, agora fica com 15% de aumento totalizando R${:.2f}'.format(salario, novosalario))