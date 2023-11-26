from time import sleep
c = ('\033[m',          #0semcores
     '\033[0;30;41m',   #1vermelho
     '\033[0;30;42m',   #2verde
     '\033[0;30;43m',   #3amarelo
     '\033[0;30;44m',   #4azul
     '\033[0;30;45m',   #5roxo
     '\033[7;30m'       #6branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#programa principal
comando = ''
while True:
    titulo(' SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo(' ATÉ LOGO ', 1)