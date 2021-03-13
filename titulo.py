

# Você recebe um arquivo chamado "books.txt" com títulos de livros, 
# cada um em uma linha separada. Para codificar os títulos dos livros, 
# você precisa pegar as primeiras letras de cada palavra do título e combiná-las.

# Complete o programa para ler o título do livro do arquivo e 
# produzir as versões codificadas, cada uma em uma nova linha.

file = open("books.txt", "r")

#your code goes here
for linha in file.readlines():
	titulo = linha.split()
	# print(titulo)
	for palavra in titulo:
		print(palavra[0], end='')
	print()
file.close()