str1= input('Digite uma string: ')
str2= input('Digite outra String: ')

tamanho1= len(str1)
tamanho2= len(str2)

print(f'"{str1}": {tamanho1} caracteres')
print(f'"{str2}": {tamanho2} caracteres')

comparacao_de_tamanho = "diferentes"
comparacao_de_conteudo = "diferente"

if str1 == str2:
  comparacao_de_tamanho = 'iguais'
  comparacao_de_conteudo = 'igual'
elif tamanho1 == tamanho2:
  comparacao_de_tamanho = 'iguais'
print(f'As duas strings são de tamanhos: {comparacao_de_tamanho}.')
print(f'As duas strings possuem : {comparacao_de_conteudo}.')