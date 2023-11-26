n = 4
maior = 0
while n != 5 or n == 4:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print("""[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa""")
    n = int(input('Digite a sua opção: '))
    if n == 1:
        print('A soma entre os dois números é: {}'.format(n1+n2))
    elif n == 2:
        print('A multiplicação entre os dois números é: {}'.format(n1*n2))
    elif n == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O número maior entre os dois números digitados é {}'.format(maior))
    elif n == 4:
        print('Digite os novos números...')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print("""[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa""")
        n = int(input('Digite a sua opção: '))
    else:
        print('Opção inválida...')
print('Saindo do programa..')
