#Q10-Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

from num2words import num2words
numero = int( input('Digite um número de  0 á 99 : ') )
num_ptbr = num2words(numero, lang='pt-br')
print(f'Número: {num_ptbr}')