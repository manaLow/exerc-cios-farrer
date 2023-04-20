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
	total_compr = float()
	total_vend = float()
	total_lucro = float()
	nome = str()
	lucromenor = float()
	lucromedio = float()
	lucromaior = float()

	nome = str(input())
	pre_compr = float(input())
	pre_vend = float(input())

	while (nome != '0'):
		
		lucro_liq = pre_vend - pre_compr

		if lucro_liq < (pre_compr*(10/100)):
			lucromenor += 1
		elif lucro_liq > (pre_compr*(20/100)):
			lucromaior += 1
		else: 
			lucromedio += 1

		total_compr += pre_compr
		total_vend += pre_vend
		total_lucro += lucro_liq 

		nome = str(input())
		pre_compr = float(input())
		pre_vend = float(input())

	print(f"Quantd. mercadorias lucro até 10%: {lucromenor}")
	print(f"Quantd. mercadorias lucro entre 10% e 20%: {lucromedio}")
	print(f"Quantd. mercadorias lucro maior que 20%: {lucromaior}")
	print("\n")
	print(f"Valor total de compra: R$ {total_compr}")
	print(f"Valor total de venda: R$ {total_vend}")
	print(f"Valor total de lucro: R$ {total_lucro}")



if __name__ == "__main__":
	main()

