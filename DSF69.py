tot18 = toth = totm20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]').strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N}: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'TOTAL DE PESSOAS COM 18 ANOS {tot18}')
print(f'AO TODO TEMOS {toth} HOMENS CADASTRADOS')
print(f'TEMOS {totm20} MULHERES COM MENOS DE 20 ANOS')