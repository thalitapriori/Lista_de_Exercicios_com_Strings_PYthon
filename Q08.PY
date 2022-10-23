#Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. 
#Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma
#onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.



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