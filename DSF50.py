somapares = cont = 0
for c in range(1,7):
    n = int(input('Digite o {} número: '.format(c)))
    if (n % 2 == 0):
        somapares += n
        cont += 1
print('A soma apenas {} numeros dos pares digitados fica {}'.format(cont,somapares))
