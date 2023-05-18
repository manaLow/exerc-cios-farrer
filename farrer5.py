
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
