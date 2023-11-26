qtd = soma = n = 0
print('Condição de parada [ 999 ]')
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        qtd += 1
print('Paramos o programa porque 999 foi digitado!')
print('Relatório: digitamos {} números e a soma deles foi {}'.format(qtd,soma))