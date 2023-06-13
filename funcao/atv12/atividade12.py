# Manuely Meireles Lemos
import mod12

def main():
    # Declaração de variáveis
    a = float()
    b = float()
    c = float()
    ma = float()
    mb = float()
    mc = float()
    area = float()
    peri = float()
    maiorare = float()
    medper_eqi = float()
    medper_esc = float()
    medper_iso = float()
    cont_eqi = float()
    cont_esc = float()
    cont_iso = float()
    totaltri = float()
    totalnaot = float()
    totalqt = float()
    percent = float()
    percetri = float
    sp = float()
    tipotriang = str()

    # Inicio variáveis
    maiorare = -1
    cont_eqi = 0
    cont_esc = 0
    cont_iso = 0

    # Entrada
    a = float(input())
    b = float(input())
    c = float(input())

    triang = mod17.checar_tr(a,b,c)

    # Processamento
    if (a != 0 and b != 0 and c != 0):
        while not(a == 0 and b == 0 and c == 0):
            if triang: # Checar se é triângulo
                peri, area, sp = mod17.periare(a,b,c)
                tipotriang = mod17.tipo_tr(a,b,c)
                if tipotriang == "EQUILATERO": 
                    medper_eqi += peri
                    cont_eqi += 1
                else:
                    if tipotriang == "ISOSCELES": 
                        medper_iso += peri
                        cont_iso += 1 
                    else:
                        medper_esc += peri
                        cont_esc += 1
                print(f"AREA = {area:.2f} PERIMETRO = {peri:.2f} TIPO = {tipotriang}") 
                
                if area > maiorare:
                    maiorare = area
                    ma = a
                    mb = b
                    mc = c
                
                totaltri += 1
            else:
                print("NAO TRIANGULO")
                totalnaot += 1
            
            a = float(input())
            b = float(input())
            c = float(input())

        if cont_eqi > 0:
            medper_eqi = (medper_eqi/cont_eqi)
        else:
            medper_eqi = 0.00

        if cont_iso > 0:    
            medper_iso = (medper_iso/cont_iso)
        else:
            medper_iso = 0.00

        if cont_esc > 0:    
            medper_esc = (medper_esc/cont_esc)
        else:
            medper_esc = 0.00

        totalqt = totalnaot + totaltri
        percent = (totalnaot/totalqt)*100
        percetri = (totaltri/totalqt)*100

        # Saída
        if maiorare > 0:
            print(f"A maior area = {maiorare:.2f} eh do triangulo: lado1 = {ma:.2f}, lado2 = {mb:.2f} e lado3 = {mc:.2f}")
        
        if medper_iso != 0 or medper_esc != 0 or medper_eqi != 0:
            print(f"{medper_eqi:.2f} eh o perimetro medio dos triangulos equilateros")
            print(f"{medper_iso:.2f} eh o perimetro medio dos triangulos isosceles")
            print(f"{medper_esc:.2f} eh o perimetro medio dos triangulos escalenos")
        
        print(f"Percentual de triangulos = {percetri:.2f}")
        print(f"Percentual de nao triangulos = {percent:.2f}")

    else:
        # Saída
        print("NAO HA DADOS PARA PROCESSAR")


if __name__ == "__main__":
    main()