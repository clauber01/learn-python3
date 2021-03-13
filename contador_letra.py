text = "hello"
dict = {}
#your code goes here

# Dada uma string como entrada, você precisa mostrar 
# quantas vezes cada letra  aparece na string.
# 
# Você decide armazenar os dados em um dicionário, 
# com as letras como chaves e as contagens correspondentes como os valores.
#
# Crie um programa para receber uma string como entrada e gerar um 
# dicionário, que representa a contagem de letras.

for letra in text:
	dict[letra] = text.count(letra)
	
print(dict)
