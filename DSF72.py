#Tuplas são imutáveis
while True:
    extenso = ('zero', 'um', 'dois', 'tres', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze','quatorze',
               'quinze', 'dezesseis', 'dezesete', 'dezoito',
               'dezenove', 'vinte')
    n = int(input('Digite um número entre 0 e 20: '))
    if n > 20 or n < 0:
        print('Número fora do intervalo..')
    else:
        print(extenso[n])
    r = ' '
    while r not in 'SN':
        r = input('Deseja continuar? [S/N]').strip().upper()[0]
    if r == 'N':
        print('FIM DO PROGRAMA')
        break