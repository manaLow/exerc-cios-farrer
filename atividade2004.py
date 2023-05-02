# Manuely M. Lemos 
def main():
    
    # Declaração de variáveis
    num = float()
    deno = float()
    val_abs = float()
    soma = float()
    termo = float()
    # Inicialização de variáveis
    soma = 0
    num = 4
    deno = 1
    termo = num/deno
    # Processamento
    while abs(termo) >= 0.0001:
        soma += termo
        num = num*(-1)
        deno += 2
        termo = num/deno
        print("soma=",termo,"=",soma) #Saída

        
if __name__ == "__main__":
    main()