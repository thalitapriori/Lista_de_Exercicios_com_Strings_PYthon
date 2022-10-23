#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
#EXEMPLO: Data de Nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.


dia, mês, ano = input('Data de nascimento: (dd/mm/aaaa): ').split('/')
meses = ['janeiro','fevereiro','março','abril',
         'maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro']
print ('Você nasceu em:')
print ('%s de %s de %s' %(dia, meses[int(mês) - 1], ano))