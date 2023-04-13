# 1.12.4. Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele
# comercializa. Para isto, mandou digitar uma linha para cada mercadoria com nome, preço de
# compra e preço de venda das mesmas. Fazer um algoritmo que:determine e escreva quantas
# mercadorias proporcionam:
# lucro < 10%
# 10% <= lucro <= 20%
# lucro > 20%
# determine e escreva o valor total de compra e de venda de todas as mercadorias, assim como
# o lucro total.
# Observação: o aluno deve adotar um flag.

def main():
	pre_compr = float()
	pre_vend = float()
	lucro_liq = float()
	lucro = float()
	total_compr = float()
	total_vend = float()
	total_lucro = float()
	nome = str()
	lucro_menor = list()
	lucro_medio = list()
	lucro_maior = list()

	lucro_menor = []
	lucro_medio = []
	lucro_maior = []

	nome = input()
	pre_compr = float(input())
	pre_vend = float(input())

	while nome != '0':
		lucro_liq = pre_vend - pre_compr
		total_compr += pre_compr
		total_vend += pre_vend
		total_lucro += lucro_liq
		lucro = (lucro_liq*100)/pre_compr

		if lucro < 10:
			lucro_menor.append(nome)
			lucro_menor.append(lucro)
		elif 10 <= lucro <= 20:
			lucro_medio.append(nome)
			lucro_medio.append(lucro)
		else:
			lucro_maior.append(nome)
			lucro_maior.append(lucro) 
		nome = input()
		pre_compr = float(input())
		pre_vend = float(input())

	print(f"Valor total de compra: {total_compr}")
	print(f"Valor total de venda: {total_vend}")



if __name__ == "__main__":
	main()

