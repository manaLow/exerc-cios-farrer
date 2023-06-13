def checar_tr(a:float,b:float,c:float)->bool:
    return (a<b+c and b<a+c and c<a+b)

def tipo_tr(a:float,b:float,c:float)->tuple:

    if a==b and b==c: # Checar se todos os lados são iguais
        tipotriang = "EQUILATERO"
    else:
        if a==b or c==b or a==c: # Se ao menos 2 lados são iguais
            tipotriang = "ISOSCELES"
        else:
            tipotriang = "ESCALENO" 
    
    return tipotriang

def periare(a:float,b:float,c:float)->tuple:
   
   peri = a + b + c
   sp = peri/2
   area = (sp*(sp-a)*(sp-b)*(sp-c))**(1/2)

   return peri,area,sp

