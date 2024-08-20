print('-=-' * 20)
velocidade = int(input('Qual velocidade o carro estava ? '))
multa = (velocidade - 80) * 7
if velocidade >= 80:
    print('O motorista estava utaprassando a velocidade e sua multa é {:.2f}'.format(multa))
else:
    print('O motorista está nas normas!')
