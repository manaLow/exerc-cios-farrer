import mod19

def main():
    
    # Variáveis
    a = float()
    b = float()
    area = float()

    a = float(input())
    b = float(input())

    while not(a==0 and b==0):
        area = mod19.c_area(a,b)
        print(f"AREA={area:.5f} A={a:.5f} B={b:.5f}")
        a = float(input())
        b = float(input())
        
if __name__== "__main__":
    main()