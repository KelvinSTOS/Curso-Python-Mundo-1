#num = int(input('Digite um número'))
#n = str(num)
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Analisando o número é {}'.format(num))
#print('A unidade é :{}'.format(u))
#print('A dezena é :{}'.format(d))
#print('A centena é :{}'.format(c))
#print('A milhar é :{}'.format(m))

num = int(input('Digite um valor'))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o vloar...')
print('A unidade do valor {} é {}'.format(num, u))
print('A dezena do valor {} é {}'.format(num,d))
print('A centena do valor {} é {}'.format(num, c))
print('O milhar desse mesmo valor é '.format(num , m))
