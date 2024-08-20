frase  = str(input('Diga-me uma frase:')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra que apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
