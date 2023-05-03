# Manuely M. Lemos 
def main():
    
    # Declaração de variáveis
    num = float()
    deno = float()
    val_abs = float()
    soma = float()
    termo = float()
    cont = int()
    # Inicialização de variáveis
    soma = 0
    num = 4
    deno = 1
    termo = num/deno
    cont = 0
    # Processamento
    while abs(termo) >= 0.01:
        cont += 1
        soma += termo
        print(num,'/',deno)
        num = num*(-1)
        deno += 2
        termo = num/deno
    print(cont)

        
if __name__ == "__main__":
    main()