texto = input("Digite um texto: ")

# inverte a string
texto_inverso = texto[::-1]

# remove os espaços em branco
texto = texto.replace(" ","")
texto_inverso = texto_inverso.replace(" ","")

# verifica se texto é igual ao texto_inverso

if (texto.lower() == texto_inverso.lower()):
    print("Palíndromo")
else:
    print("Não é palíndromo")