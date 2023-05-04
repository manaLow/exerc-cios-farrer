""". Fazer um algoritmo para calcular a raiz quadrada de um número positivo, usando o
roteiro abaixo, baseado no método de aproximações sucessivas de Newton:
Seja Y o número:
• A primeira aproximação para a raiz quadrada de Y é X1 = Y/2
• as sucessivas aproximações serão: Xn+1 = (Xn
2 + Y)/2Xn
O algoritmo deverá prever 20 aproximações."""

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
			print(f"{cont}ª APROXIMAÇÃO = {x:.5f}")
	else:
		print("Não existe raiz quadrada REAL")  

if __name__ == "__main__":
	main()