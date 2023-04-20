'''
Supondo que a população de um país A seja da ordem de 90.000.000 de habitantes
com uma taxa anual de crescimento de 3% e que a população de um país B seja,
aproximadamente, de 200.000.000 de habitantes com uma taxa anual de crescimento de 1,5%,
fazer um algoritmo que calcule e escreva o número de anos necessários para que a população
do país A ultrapasse ou iguale a população do país B, mantidas essas taxas de crescimento.

'''
def main():
	# declaração de variáveis 
	paisa = int()
	paisb = int()
	taxa = float()
	taxb = float()
	anos = int()

	paisa = 90000000
	paisb = 200000000
	taxa = 0.03
	taxb = 0.015
	anos = 0

	while paisb >= paisa:
		anos += 1
		paisa += (paisa*taxa)
		paisb += (paisb*taxb)

	print(anos)

if __name__ == "__main__":
	main()
