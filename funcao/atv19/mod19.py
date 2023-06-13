def c_area(a:float,b:float)->float:

    y0 = float()
    x0 = float()

    if a == 0 or b == 0:
        return 0
    else: 
        y0 = b
        x0 = -b/a
        area = abs((y0 * x0)/2)
        return area
