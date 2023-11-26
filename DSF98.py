from time import sleep
def contador(i,f,p):
    print(f'Contando do valor {i} até {f}, de {p} em {p}...')
    if p < 0 :
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.1)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.1)
            cont -= p
        print('FIM')

contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar essa contagem!!!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)

"""from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end = ' ')
        sleep(0.5)
    print()




contador(1,10,0)
contador(10,0,2)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))"""