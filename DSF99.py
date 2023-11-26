from time import sleep
def maior(* num):
    nmaior = pos = 0
    if len(num) == 1:
        nmaior = num[0]
    else:
        while pos < len(num):
            if num[pos] > nmaior:
                nmaior = num[pos]
            pos += 1
    print('-=-' * 25)
    print('Analisando os valores passados......')
    tot = 0
    for i in num:
        print(f'{i}', end=' ')
        sleep(0.2)
        tot += 1
    print(f'Foram digitados {tot} valores ao todo..')
    print(f'O maior valor digitado foi {nmaior}')
    print('-=-' * 25)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()