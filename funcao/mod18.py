
def c_2mdc(a:int,b:int)->int:

    rest = int()

    rest = a%b
    
    if rest != 0:
        while rest != 0:
            a = b
            b = rest
            rest = a%b
        return b
    else:
        return b

def c_3mdc(a:int,b:int,c:int)->int:

    calc = int()
    mdc = int()

    calc = c_2mdc(a,b)
    mdc = c_2mdc(calc,c)

    return mdc