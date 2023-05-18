# Soma de todos os números primos de 4 algarismos
# conte quantos divisores o número tem entre 1 e ele mesmo
def main():

	num = int()
	cont = int()
	primo = int()
	soma = int()
	i = int()

	cont = 0
	soma = 0

	for num in range(1000,10000):
		cont = 0
		for i in range(1,num+1):
			if num%i == 0:
				cont += 1
		if cont <= 2:
			primo += 1
			soma += num

	print("Soma:",soma, "\nQuantidade de números primos:",primo)

if __name__ == '__main__':
	main()

