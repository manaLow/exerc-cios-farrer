import mod20

def main():
    
    n = int()
    quant = int()

    n = int(input())

    while n > 0:
        quant = mod20.c_quantdiv(n)
        if quant == 1:
            print(f"{n} POSSUI 1 DIVISOR")
        else:
            print(f"{n} POSSUI {quant} DIVISORES")
        n = int(input())


if __name__ == "__main__":
    main()