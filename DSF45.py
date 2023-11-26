# Jokenpô ou Pedra,papel e tesoura
import random
import time
print('Hora do jogo!!')
print('[1]PEDRA\n[2]PAPEL\n[3]TESOURA')
dados = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = int(input('DIGITE SUA JOGADA: ')) - 1
jogadausuario = (dados[escolha])
print('aguarde a jogada do pc...')
time.sleep(1)
jogadapc = random.choice(dados)
if jogadausuario == 'PEDRA':
    if jogadapc == 'TESOURA':
        print('A PEDRA GANHA DA TESOURA')
        print('PARABÉNS, VOCÊ GANHOU!!')
    elif jogadapc == 'PAPEL':
        print('A PEDRA PERDE DO PAPEL')
        print('VOCÊ PERDEU')
    else:
        print('EMPATE')
elif jogadausuario == 'PAPEL':
    if jogadapc == 'PEDRA':
        print('O PAPEL GANHA DA PEDRA')
        print('PARABÉNS, VOCÊ GANHOU!!')
    elif jogadapc == 'TESOURA':
        print('O PAPEL PERDE DA TESOURA')
        print('VOCÊ PERDEU')
    else:
        print('EMPATE')
elif jogadausuario == 'TESOURA':
    if jogadapc == 'PAPEL':
        print('A TESOURA GANHA DO PAPEL')
        print('PARABÉNS, VOCÊ GANHOU')
    elif jogadapc == 'PEDRA':
        print('A TESOURA PERDE DA PEDRA')
        print('VOCÊ PERDEU')
    else:
        print('EMPATE')
print('APENAS LEMBRANDO AS JOGADAS.... seu palpite {} e jogada do pc {}'.format(dados[escolha], jogadapc))
#pense também caso ele digita um número maior que 3
