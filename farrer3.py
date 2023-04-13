# 1.12.3. A conversão de graus Farenheit para centígrados é obtida por
# C = 5/9 x (F - 32)
# Fazer um algoritmo que calcule e escreva uma tabela de centígrados em função de graus
# Farenheit, que variam de 50 a 150 de 1 em 1.

def main():

	c = int()

	for f in range(50, 151, 1):
		
		c = 5/9 * (f-32)

		print(f'Farenheit: {f}°; Centígrados: {c:.2f}°')


if __name__ == "__main__":
	main()