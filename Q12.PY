numero = int(input('Digite o numero do Telefone: '))

novoNumero = ''
if len(str(numero)) < 8:
    diferenca = 8 - len(str(numero))
    novoNumero = '3' * diferenca

numeroFormatado = novoNumero + str(numero)
numeroFormatado = numeroFormatado[0:4] + '-' + numeroFormatado[5:]

print('O numero do telefone possui %d dígitos. Vou acrescentar o digito três na frente.' % len(str(numero)))

print('O numero do Telefone corrigido sem formatação: %d' % numero)

print('O numero corrigido com formatação: %s' % numeroFormatado)        