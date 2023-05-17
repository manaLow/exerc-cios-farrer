# Manuely Meireles Lemos
def main():

	# Variáveis
	totalpeca = int()
	pagfab = float()
	salario = float()
	numop = int()
	pecaop = int()
	sexo = str()
	medpecas_ha = float()
	medpecas_hb = float()
	medpecas_hc = float()
	medpecas_ma = float()
	medpecas_mb = float()
	medpecas_mc = float()
	maiorsal = float()
	maiorsalop = int()
	contam = float()
	contbm = float()
	contcm = float()
	contah = float()
	contbh = float()
	contch = float()

	#Constante
	SAL_MIN = 1320
        
	# Inicio de variáveis
	salario = SAL_MIN
	maiorsal = -1
	contam = 0
	contbm = 0
	contcm = 0
	contah = 0
	contbh = 0
	contch = 0

	# Entrada de dados
	numop = int(input())
	
	# Processamento
	while numop != 0:
		pecaop = int(input())
		sexo = str(input())

		if pecaop <= 30: # Cálculo classe a
			salario = SAL_MIN
			if sexo == "F": # mulheres
				contam += 1
				medpecas_ma += pecaop
			else:
				contah += 1 # homens
				medpecas_ha += pecaop
			totalpeca += pecaop
			pagfab += salario
			print(f"Operário {numop} - SALÁRIO = {salario:.2f}")

		elif pecaop >= 30 and pecaop <= 35:
			salario = SAL_MIN  + (SAL_MIN*0.03*(pecaop-30))
			if sexo == "F": # mulheres
				contbm += 1
				medpecas_mb += pecaop
			else:
				contbh += 1 # homens
				medpecas_hb += pecaop
			totalpeca += pecaop
			pagfab += salario
			print(f"Operário {numop} - SALÁRIO = {salario:.2f}")

		else:
			salario = SAL_MIN + (SAL_MIN*0.05*(pecaop-30))
			if sexo == "F": # mulheres
				contcm += 1
				medpecas_mc += pecaop
			else:
				contch += 1 # homens
				medpecas_hc += pecaop
			totalpeca += pecaop
			pagfab += salario
			print(f"Operário {numop} - SALÁRIO = {salario:.2f}")

		if salario > maiorsal: # maior salário
			maiorsal = salario
			maiorsalop = numop

		numop = int(input()) # próximo operário


	# Cálculo média das classes
	medpecas_ha = (medpecas_ha/contah)
	medpecas_hb = (medpecas_hb/contbh)
	medpecas_hc = (medpecas_hc/contch)
	medpecas_ma = (medpecas_ma/contam)
	medpecas_mb = (medpecas_mb/contbm)
	medpecas_mc = (medpecas_mc/contcm)

	# Saída
	print(f"Folha de pagamento total da fábrica = {pagfab:.2f} \nTotal peças/mês = {totalpeca}")
	print(f"\nMédia de peças produzidas por homens e mulheres dividido por classe:")
	print(f"Homens:\nCLASSE A = {medpecas_ha:.2f}\nCLASSE B = {medpecas_hb:.2f}\nCLASSE C = {medpecas_hc:.2f}")
	print(f"Mulheres:\nCLASSE A = {medpecas_ma:.2f}\nCLASSE B = {medpecas_mb:.2f}\nCLASSE C = {medpecas_mc:.2f}")
	print(f"\nOperário com maior salário: \n OPERÁRIO {maiorsalop} - SALÁRIO = {maiorsal:.2f}")


if __name__ == "__main__":
    main()