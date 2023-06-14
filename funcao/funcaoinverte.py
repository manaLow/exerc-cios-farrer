def f_invertealgarismo(n):
    invertido = int()
    invertido = 0
    while n > 0:
        d = n%10
        invertido = invertido*10 + d
        n = n//10
    
    return invertido