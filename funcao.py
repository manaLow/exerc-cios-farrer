
def calc_fatorial(n:int)->int:
	i = int()
	fat = int()
	fat = 1
	for i in range(n,1,-1):
		fat = fat * i
	return fat

def calc_imc(peso:int,altura:int)->int:
	imc = peso/(altura*altura)
	return imc

def class_imc()


def main():

	n = int()
	fat = int()

	n = int(input())
	fat = calc_fatorial(n)
	print(n,fat)

if __name__ == "__main__":
	main()