dist = float(input('Distância da sua viagem? KM:'))
print('Você está preste a iniciar uma viagem de {}KM'.format(dist))
if dist <= 200:
    pre = dist * 0.50
else:
    pre = dist * 0.30
print('E o preço da sua passagem é, {}$'.format(pre))
