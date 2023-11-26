preco = float(input('Digite o preço do produto: R$'))
#precocomdesconto = (preco*0.95)
#calculo com decimal é bem mais prático
desconto = (preco*5)/100
precocomdesconto = preco - desconto
print('O preco do produto R${:.2f}, na liquidacao com 5% de desconto fica R${:.2f}'.format(preco,precocomdesconto))