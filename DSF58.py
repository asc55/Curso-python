from random import randint
npalpites = 1
sorteado = randint(1,10)
palpite = int(input('Tente adivinhar o número sorteado entre 1 - 10: '))
while palpite != sorteado:
    npalpites += 1
    if palpite > sorteado:
        print('menos...')
        palpite = int(input('Tente novamente, digitando um novo palpite: '))
    else:
        print('mais...')
        palpite = int(input('Tente novamente, digitando um novo palpite: '))
print('Você finalmente conseguiu acertar depois de {} palpites..'.format(npalpites))