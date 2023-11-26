km = float(input('Quantos km de extensão da viagem: '))
if km <= 200:
    custo = km*0.50
    print('Sua viagem de {}km, fica no valor de {}...'.format(km,custo))
else:
    custo = km*0.45
    print('Sua viagem de {}km, fica no valor de {}'.format(km,custo))