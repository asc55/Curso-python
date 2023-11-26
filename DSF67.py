#Tabuadas até digitar num negativo
n = i = 0
while True:
    n = int(input('Tabuada de qual número: '))
    if n > 0:
        for i in range(1,11):
                print('{} X {} = {}'.format(n,i,n*i))
    else:
        print('PROGRAMA TABUADA ENCERRADO, NÃO É POSSÍVEL num negativos')
        break