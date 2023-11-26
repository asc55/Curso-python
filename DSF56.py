#A média de idade do grupo, o nome do homem mais velho e quantas mulheres com menos de 20 anos
hmaior = maior = somaidades = totm20 = 0
nomeh = ''
for c in range(1,5):
    nome = input('Digite o nome da {} pessoa: '.format(c))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = int(input('[ 1 ] MASCULINO\n[ 2 ] FEMININO\nSEXO:'))
    if idade >= 1:
        somaidades += idade
    if sexo == 1:
        if idade > maior:
            maior = idade
            nomeh = nome
    elif sexo == 2 and idade < 20:
            totm20 += 1
print('A média da idade do grupo é igual a {:.2f}'.format(somaidades/4))
print('O nome do homem mais velho é {} com {} anos'.format(nomeh,maior))
print('A quantidade de mulheres com menos de 20 anos é igual a {}'.format(totm20))