import mod20

def main():

    a = int()
    b = int()
    tabuad = str()

    a = int(input())
    b = int(input())

    for x in range(a,b+1):
        tabuad = mod20.tabuada(x)
        print(tabuad)

if __name__=="__main__":
    main()