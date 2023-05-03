import math


def main():

	# Declaração de variáveis
	deno = float()
	nume = float()
	x = float()
	expo = float()
	valor = int()
	exato = float()
	dif = float()
	i = float()

	# Entrada
	x = float(input())

	deno = 1
	i = 1
	expo = 0 
	exato = math.exp(x)
	valor = 1
	dif = abs(exato - valor)

	while dif > 0.0001:
		nume = x**i
		deno = deno*i
		valor = valor + (nume/deno)
		i += 1
		dif = abs(exato - valor)
		
	print(valor,i)


if __name__ == "__main__":
	main()