frase = input('Digite a frase: ')
branco = 0
vogais = 0
for f in frase:
    if f == '':
        branco += 1
    if f in 'a''e''i''o''u':
        vogais += 1

print('Total de espaços em branco: %d' % branco)
print('Total de vogais: %s' % vogais)
