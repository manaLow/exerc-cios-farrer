
def main():

	c = int()

	for f in range(50, 151, 1):
		
		c = 5/9 * (f-32)

		print(f'Farenheit: {f}°; Centígrados: {c:.2f}°')


if __name__ == "__main__":
	main()