# Manuely M. Lemos
def main():

    # Declaração de Variáveis
    t1 = float()
    t2 = float()
    t3 = float()
    tempo_etap1 = float()
    tempo_etap2 = float()
    tempo_etap3 = float()
    dif1 = float()
    dif2 = float()
    dif3 = float()
    pontos1 = float()
    pontos2 = float()
    pontos3 = float()
    total = float()
    inscricao = int()
    vencedor = int()
    maior_pont = float()


    # Entrada de Dados
    t1 = float(input())
    t2 = float(input())
    t3 = float(input())

    inscricao = 0
    maior_pont = 0

    while inscricao != 9999:
        # Número de inscrição
        inscricao = int(input())
        
        # Processamento
        if inscricao != 9999:

            tempo_etap1 = float(input())
            tempo_etap2 = float(input())
            tempo_etap3 = float(input())
            
            while inscricao != 9999:
            
                dif1 = abs(tempo_etap1 - t1)
                dif2 = abs(tempo_etap2 - t2)
                dif3 = abs(tempo_etap3 - t3)

                if dif1 < 3:
                    pontos1 = 100
                elif dif1 >= 3 and dif1<=5:
                    pontos1 = 80
                else:
                    pontos1 = 80 - ((dif1-5)/5)

                if dif2 < 3:
                    pontos2 = 100
                elif dif2 >= 3 and dif2<=5:
                    pontos2 = 80
                else:
                    pontos2 = 80 - ((dif2-5)/5)

                if dif3 < 3:
                    pontos3 = 100
                elif dif3 >= 3 and dif3<=5:
                    pontos3 = 80
                else:
                    pontos3 = 80 - ((dif3-5)/5)

                total = pontos1 + pontos2 + pontos3

                # Saída
                print(f"EQUIPE={inscricao} P1={pontos1:.2f} P2={pontos2:.2f} P3={pontos3:.2f} PT={total:.2f}")

                # Maior pontuação
                if total > maior_pont:
                    maior_pont = total
                    vencedor = inscricao

                inscricao = int(input())
                
                if inscricao != 9999:
                    tempo_etap1 = float(input())
                    tempo_etap2 = float(input())
                    tempo_etap3 = float(input())
            
            # Saída
            print(f"EQUIPE VENCEDORA={vencedor} PONTUACAO TOTAL={maior_pont:.2f}")
        else:
            print("SEM EQUIPES CADASTRADAS")
                

if __name__ == "__main__":
    main()