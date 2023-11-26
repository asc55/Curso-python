print('-=-'*25,'\n',' '*25, 'LISTAGEM DE PREÇOS',' '*25)
listagem = ('Pão francês','2.00','Mortadela','3.50','Linguiça','5.00',
            'Queijo Qualho','7.50','Queijo Mussarela','9.50',
            'Refrigerante','2.90','Kisuco da Eliana','0.15',
            'Pitu','4.00','Cerveja','2.15','Manteiga','1.50')
"""for cont in range(0,20,2):
    print(f'{listagem[cont]:30}', end='..'*25)
    print('R$',listagem[cont+1])"""
"""print(listagem[0],'.'*25, 'R$',listagem[1])
print(listagem[2],'.'*25, 'R$',listagem[3])
print(listagem[4],'.'*25, 'R$',listagem[5])
print(listagem[6],'.'*25, 'R$',listagem[7])
print(listagem[8],'.'*25, 'R$',listagem[9])
print(listagem[10],'.'*25, 'R$',listagem[11])
print(listagem[12],'.'*25, 'R$',listagem[13])
print(listagem[14],'.'*25, 'R$',listagem[15])
print(listagem[16],'.'*25, 'R$',listagem[17])
print(listagem[18],'.'*25, 'R$',listagem[19])"""

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>3}')
print('-=-'*25)