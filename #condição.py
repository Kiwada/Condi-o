#condição
n1 = float(input('digite a primeira nota:'))
n2 = float(input('digite a segunda nota:'))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua Média foi boa! PARABÉNS!')
else:
    print('Sua media foi ruim! Estude MAIS')