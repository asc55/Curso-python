from datetime import date
data = date.today().year
print('-=-'*20)
print('ALISTAMENTO MILITAR')
nasc = int(input('Digite o ano de nascimento: '))
idade = (data - nasc)
if idade == 18:
    print('Você tem {} anos, momento do alistamento.'.format(idade))
elif idade < 18:
    prazo = (18-idade)
    print('Você ainda irá se alistar, restam ainda {} anos já que sua idade é {}.'.format(prazo,idade))
    print('SEU ALISTAMENTO {}'.format(data+prazo))
else:
    prazo = (idade-18)
    print('Você já se alistou há {} anos já que sua idade é {}.'.format(prazo,idade))
    print('SEU ALISTAMENTO {}'.format(data-prazo))