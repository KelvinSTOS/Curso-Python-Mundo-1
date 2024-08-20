n1 = float(input('1° Nota 1° Bimestre?'))
n2 = float(input('2° Nota 1° Bimestre?'))
m1 = (n1 + n2 ) / 2
if m1 >= 6.0:
    print('A nota do aluno foi {} e ele(a)  passou do 1° Bimestre, Parabéns!'.format(m1))
else:
    print('O aluno não passou do 1° Bimestre, precisará repetir')
print('2° Bimetres no ano') 
n3 = float(input('3° Nota 2° Bimetre?')) 
n4 = float(input('4° Nota 2° Bimestre?'))
m2 =(n3 + n4) / 2
if m2 >= 6.0:
    print('A nota do aluno foi {} e ele(a) passou do 2° Bimestre, Parabens'.format(m2))
else:
    print('O aluno não passou do 2° Bimestre, precisará repetir')
n5 = float(input('5° Nota 3° Bimestre?'))
n6 = float(input('6° Notas 3° Bimestre?'))
m3 = (n5 + n6) / 2
if m3 >= 6.0:
    print('A nota do aluno foi {} e ele(a) passou do 3° Bimestre, Parabéns!'.format(m3))
else:
    print('O aluno não passou do 3° Bimestre')
NF = (m1 + m2 + m3) / 3
if NF >=6.0:
    print('O Aluno PASSOU DE ANO, PARABÉNS!')
else:
    print('INFELIZMENTE O ALUNO NÃO PASSOU DE ANO :(')
