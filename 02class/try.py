nome = input("Insira uma string aqui: ")

try:
	resultado = len(nome)
	print(resultado)
except TypeError as e:
	print(e) # imprime a mensagem de erro, pode colocar em log
else: # se der tudo certo e não acabar no except
	print("Tudo ok")
finally: # Sempre ocorre, independente se der erro ou tudo bem
	print("Programa finalizado")