#Situação escolar
n1 = float(input('Digite a sua nota 1: '))
n2 = float(input('Digite a sua nota 2: '))
media = (n1 + n2)/2
if media < 5:
    print('Você está REPROVADO, media de {}'.format(media))
elif 5.0 < media < 7:
    print('Você está em RECUPERAÇÃO, media de {}'.format(media))
else:
    print('Você está APROVADO com media de {}'.format(media))
