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
	qtd = int()

	qtd = int(input())

	for num in range(qtd):
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
			
		print(f"X={x:.6f} EXP_FUNCAO({x:.6f})={exato:.6f} EXP_SERIE({x:.6f})={valor:.6f}")


if __name__ == "__main__":
	main()