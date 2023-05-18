# Manuely Meireles Lemos

def main():

	# Declaração de variáveis
	y = float()
	x = float()
	cont = int()

	# Entrada 
	y = float(input())
	x = y/2
	cont = 0

	# Processamento
	if y > 0:

		print(f"Y={y:.5f}")
		for _ in range(1,20):
			x = ((x**2)+y)/(2*x)
			cont += 1
			print(f"{cont}ª APROXIMAÇÃO = {x:.5f}") # Saída
	else:
		print("Não existe raiz quadrada REAL")  # Saída

if __name__ == "__main__":
	main()