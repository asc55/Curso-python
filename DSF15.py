#Aluguel de Carros
dias = int(input('Quantos dias de aluguel: '))
km = float(input('Quantos km foram rodados: '))
valordias = dias*60
valorkm = km*0.15
valortotal = valorkm + valordias

print('Alugando o carro por {} dias e rodando {} km, o valor total fica R${}'.format(dias,km,valortotal))