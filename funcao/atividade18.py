import mod18

def main():
    
    # Variáveis
    a = int()
    b = int()
    c = int()
    mdc = int()

    for _ in range(25):
        a = int(input())
        b = int(input())
        c = int(input())
        mdc = mod18.c_3mdc(a,b,c)
        print(f"MDC({a}, {b}, {c})={mdc}") 
    

if __name__ == "__main__":
    main()