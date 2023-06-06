
def res_calc(n:int)->str:

    # Declaração de vars
    numhexa = str()
    letras = str()

    letras = "ABCDEF"

    # Processamento
    if n >= 10:
        numhexa = letras[n-10]
    else:
        numhexa = str(n)
    
    return numhexa


def f_hexadecimal(num10:int)->str:
    
    # Declaração de vars
    resto = int()
    quoc = int()
    hexa = str()

    hexa = ""

    quoc = num10//16
    resto = num10%16

    # Processamento
    if quoc > 15:
        hexa = res_calc(resto) + hexa
        while quoc >= 16:
            resto = quoc%16
            quoc = quoc//16
            hexa = res_calc(resto) + hexa
        hexa = res_calc(quoc) + hexa

    else:
       if quoc != 0:
            hexa = res_calc(resto) + hexa
            hexa =  res_calc(quoc) + hexa
       else:
            hexa = res_calc(resto)

    return hexa

def main():

    # Declaração de vars
    num10 = int()
    num_hexa = str()

    num10 = int(input())

    # Processamento
    while num10 >= 0:
        num_hexa = f_hexadecimal(num10)
        print(f"BASE10={num10} BASE16={num_hexa}")
        num10 = int(input())


if __name__ == "__main__":
    main()