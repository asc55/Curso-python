#Shopping
preco = float(input('Digite o preço a ser pago pelo produto: R$'))
print('Condições de pagamento:\n[1]à vista no cheque ou dinheiro\n[2]à vista no cartão\n[3]até 2x no cartão\n[4]3x ou mais no cartão')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    novopreco = preco*0.9
    print('O preço antigo de R${:.2f}, fica no valor de R${:.2f} com 10% de desconto.'.format(preco, novopreco))
elif opcao == 2:
    novopreco = preco*0.95
    print('O preço antigo de R${}, fica no valor de R${:.2f} com 5% de desconto.'.format(preco, novopreco))
elif opcao == 3:
    print('O valor continua o mesmo de R${:.2f}.'.format(preco))
elif opcao == 4:
    vezes = int(input('Quantas vezes? '))
    novopreco = preco*1.2
    parcela = novopreco/vezes
    print('O preço tem um aumento de juros de 20%, ficando em R${:.2f} em 10x de R$ {:.2f}'.format(novopreco,parcela))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO, TENTE NOVAMENTE')