valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário: R$'))
anos = int(input('Digite a quantidade de anos do financiamento: '))
prestacao = valor/(anos*12)
if prestacao <= 0.3*salario:
    print('EMPRÉSTIMO APROVADO, parcela de R${:.2f} do salário de R${}'.format(prestacao,salario))
else:
    print('EMPRÉSTIMO NEGADO, pois a parcela de 30% R${:.2f}, excede os 30% R${} do salário de R${}'.format(prestacao,0.3*salario,salario))
print('Casa no valor de R${} \nSalário de R${}\nParcela de R${:.2f}'.format(valor, salario,prestacao))