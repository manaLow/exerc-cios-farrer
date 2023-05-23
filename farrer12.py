def main():

	# Declaração de variáveis
	matr = str()
	n1 = float()
	n2 = float()
	n3 = float()
	freq = float()
	med = float()
	maoirn = float()
	maoiral = str()
	menorn = float()
	menoral = str()
	qtdrepro = int()
	reprofreq = int()
	perc_reprofreq = int()
	totalturma = float()
	medtotal = float()
	qtdal = int()
	aprov = str()
	reprov = str()

	maoirn = 0
	menorn = 999
	aprov = str("APROVADO")
	reprov = str("REPROVADO")

	matr = str(input())

	while matr != "0":
		qtdal += 1
		n1 = float(input())
		n2 = float(input())
		n3 = float(input())
		freq = float(input())
		med = (n1 + n2 + n3)/3

		totalturma += med

		if med > maoirn:
			maoirn = med
			maoiral = matr

		if med < menorn:
			menorn = med
			menoral = matr

		if (med >= 60) and (freq >= 40):
			print(f"{matr}: NOTA FINAL = {med:.2f} FREQUÊNCIA = {freq} - {aprov} ")
		else:
			qtdrepro += 1
			if freq < 40:
				reprofreq += 1
			print(f"{matr}: NOTA FINAL = {med:.2f} FREQUÊNCIA = {freq} - {reprov} ") 

		matr = str(input())

	perc_reprofreq = (100*reprofreq)/qtdal
	medtotal = totalturma/qtdal
	print(f"MAIOR NOTA DA TURMA = {maoirn:.2f} ALUNO: {maoiral}")
	print(f"MENOR NOTA DA TURMA = {menorn:.2f} ALUNO: {menoral}")
	print(f"NOTA MÉDIA DA TURMA = {medtotal:.2f}")
	print(f"TOTAL DE REPROVADOS = {qtdrepro}")
	print(f"PORCENTAGEM DE ALUNOS REPROVADOS POR FREQUÊNCIA = {perc_reprofreq:.2f}")


if __name__ == "__main__":
	main()