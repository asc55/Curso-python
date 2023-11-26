soma = valores = 0
for c in range(1,500,2):
    if (c % 3 == 0):
        soma += c
        valores += 1
print('A soma dos {} números ímpares entre 1 e 500, e que são múltiplos de 3 é igual a {}'.format(valores,soma))