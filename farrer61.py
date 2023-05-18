# Manuely Meireles Lemos
def main():

	# Declaração de variáveis
	n1 = int()
	n2 = int()
	n3 = int()

	# Processamento
	for num in range(1000,10000):
		n1 = num//100
		n2 = num%100
		n3 = (n1+n2)**2

		if n3 == num:
			print(n3) # Saída


if __name__ == "__main__":
	main()