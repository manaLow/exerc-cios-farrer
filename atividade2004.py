# Manuely M. Lemos 
def main():
    
    # Declaração de variáveis
    n = int(input())
    soma = int()
    numero = int()
    # Processamento
    while (n != 0):
        soma = 0
        for numero in range(1, n+1):
            soma += numero
        print(f"SOMA={soma}") # Output

        n = int(input())
        
if __name__ == "__main__":
    main()