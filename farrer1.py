# 1.12.1. Fazer um algoritmo que:
# - Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. A
# última linha que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule e
# escreva a idade média deste grupo de indivíduos.

def main():

	idade = int()
	soma = int()
	soma_idade = int()
	total = int()
	media = float()
	
	idade = int(input())
	while idade != 0:
		soma_idade += idade
		soma += 1
		media = soma_idade/soma
		idade = int(input())

	print (f'Média de idade: {media}')

if __name__ == "__main__":
	main()