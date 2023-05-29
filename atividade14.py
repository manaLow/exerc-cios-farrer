def main():

    # Declaração de variáveis
    texto = str()
    qtd_r = int()

    # Iniciar variáveis
    qtd_r = 0

    # Entrada de dados
    texto = str(input())

    # Processamento
    for x in texto:
        if x == "r" or x == "R":
            qtd_r += 1
        
    print(f"Quantidade de r's = {qtd_r}")

if __name__ == "__main__":
    main()