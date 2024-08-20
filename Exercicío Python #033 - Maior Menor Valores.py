n1 = int(input("Digite o primeiro valor :"))
n2 = int(input('Digite o segundo valor :'))
n3 = int(input('Digite o terceiro valor :'))
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n2 < n1:
     menor = n3  
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
     maior = n3
print('O menor número foi {} e o maior foi {}'.format(menor, maior))
