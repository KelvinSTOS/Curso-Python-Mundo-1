preço = float(input('Qual o preço do produto?'))
novo = preço - (preço * 5 / 100)
print('Na promoção de 5% o produto de {}BRL com desconto fica {}BRL'.format(preço ,novo))
