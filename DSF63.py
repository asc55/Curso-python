#Sequência de Fibonacci
n = int(input('Quantos termos da sequência você deseja: '))-3
print('-=-'*25)
print('SEQUENCIA DE FIBONACCI')
print(0, end='..')
n1 = n2 = 1
print(n1,end='..')
print(n2,end='..')
while n != 0:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    n -= 1
    if n >= 1:
        print(n3, end='..')
    else:
        print(n3, end=' ')
