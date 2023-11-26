from random import randint
print('Vamos jogar....')
pensou = randint(0,5)
palpite = int(input('Acabei de pensar em um número, dê o seu palpite: '))
if pensou == palpite:
    print('N pensado {}, N palpite {}, PARABÉNS!!!!'.format(pensou, palpite))
else:
    print('N pensado {}, N palpite {}, NÃO FOI DESSA VEZ.'.format(pensou, palpite))