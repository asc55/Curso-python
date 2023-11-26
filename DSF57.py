sexo = input('Digite o sexo da pessoa: ').strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    sexo = input('DIGITE UM SEXO VÁLIDO: ').strip().upper()[0]
print('Sexo válido e gravado!! {}'.format(sexo))

#while sexo not in 'MmFf':