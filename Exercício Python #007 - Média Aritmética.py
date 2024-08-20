#Primeiro Bimestre
p1 = float(input('Primeira nota'))
s1 = float(input('Segunda nota'))
m1 = (p1 + s1) / 2
print('Nas notas {} e {} a média do aluno é {:.2f}'.format( p1, s1, m1))

#Segundo Bimestre
p2 = float(input('Primeira nota 2° Bimestre'));
s2 = float(input('Segunda nota 2° bimestre'));
m2 = (p2 + s2) / 2
print('Nas notas {} e {} a média do aluno é {:.2f}'.format(p2, s2, m2))

#Terceiro Bimestre

p3 = float(input('Primeira nota #3° Bimestre'))
s3 =float(input('Segunda nota 3° bimestre'))
m3 = (p3 + s3) / 2
print('Nas notas {} e {} a média é {:.2f}'.format(p3, s3, m3))

RF = (m1 + m2 + m3)/3
print('A soma dos resultado é {:.2f}'.format(RF))
