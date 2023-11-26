velocidade = float(input('Digite a velocidade do carro: '))
limite = 80
multa = (velocidade-80)*7
if velocidade > limite:
    print('MULTA!! de R${}'.format(multa))
else:
    print('Siga na estrada...')
    print('Tenha um bom dia!\n dirija com segurança')