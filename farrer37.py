def main():
	# Declaração de Variáveis
	num = float()
	deno = float()
	soma = float()
	n = float()

	deno = 1
	num = 1

	for x in range(1,50):
		
		for i in range(1,x+1):
			num = num*i
		n = num/deno
		if num%2 == 0:
			n = n*(-1)
		soma += n
		deno = 2**x
		num = 1
		
			
	print(f"{soma:.5f}")


if __name__ == "__main__":
	main()