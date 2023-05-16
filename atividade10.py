# Manuely Meireles Lemos - MATRÍCULA: 20231bsi0309
def main():

    # Declaração de variáveis
    massin = float()
    massfim = float()
    seg = int()
    hora = int()
    min = int()

    # Valores inciais
    massin = float(input())
    massfim = massin
    
    # Processamento
    while massin >= 0:
        seg = 0
        while massfim >= 0.5:
            massfim = massfim/2
            seg += 50
        min = int(seg/60)
        hora = int(min/60)
        seg = seg % 60
        print(f"MASSA INICIAL={massin:.3f} MASSA FINAL={massfim:.3f} TEMPO DECORRIDO={hora}:{min}:{seg}")

        massin = float(input())
        massfim = massin   
    print("FIM")     


if __name__ == "__main__":
    main()