import mod15

def main():

    # Declaração de vars
    num10 = int()
    num_hexa = str()

    # Entrada de dados
    num10 = int(input())

    # Processamento
    while num10 >= 0:
        num_hexa = mod15.f_hexadecimal(num10)
        print(f"BASE10={num10} BASE16={num_hexa}")
        num10 = int(input())


if __name__ == "__main__":
    main()