def c_quantdiv(n:int)->int:
    
    quant = int()

    quant = 0

    for x in range(1,n+1):
        if n%x == 0:
            quant += 1
    
    return quant