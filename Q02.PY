#Q02-Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
#Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input('Digite seu Nome: ').upper()
nome_invertido_por_letras = nome[::-1]
print(f'Nome com letras maiúscula : {nome}')
print(f'Nome com letras invertidas : {nome_invertido_por_letras}')