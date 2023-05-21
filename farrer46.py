def main():

	# Declaração de variáveis
	y1 = float()
	y2 = float()
	y = float()
	x = float()

	# Inicializando variáveis
	x = float(input())
	y = float(input())

	# Processamento
	while x!= 0 and y!=0:
		y1 = 3*x
		y2 = (1/3)*x

		if x > 0:
			if y > y2 and y < y1:
				print(f"Ponto: ({x},{y}) == INTERIOR") # Saída
			else:
				print(f"Ponto: ({x},{y}) == EXTERIOR") # Saída
		else:
			if y < y2 and y > y1:
				print(f"Ponto: ({x},{y}) == INTERIOR") # Saída
			else:
				print(f"Ponto: ({x},{y}) == EXTERIOR") # Saída

		x = float(input())
		y = float(input())

if __name__ == "__main__":
	main()