
def c_area(a,b):

    y0 = float()
    x0 = float()

    y0 = b
    x0 = -b/a

    if a == 0 or b == 0:
        return 0
    else: 
        area = abs((y0 * x0)/2)
        return area

def main():
    
    # Variáveis
    a = float()
    b = float()
    area = float()

    a = float(input())
    b = float(input())

    if a != 0:
        area = c_area(a,b)
        
if __name__== "__main__":
    main()