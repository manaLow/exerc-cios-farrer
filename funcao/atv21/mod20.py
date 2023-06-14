def tabuada(n:int)->str:

    tabu = str()

    for x in range(1,11):
        tabu += f"{n} x {x} = {n*x}\n"

    return tabu