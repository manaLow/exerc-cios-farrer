# Manuely M. Lemos
def main():
    
    # Declaração de variáveis
    n = int()
    id_turma = str()
    quant_matr = int()
    aluno = str()
    porcent_ausen = float()
    ausencias = int()
    maior_por = float()
    menor_por = float()
    turma_maior = str()
    turma_menor = str()
    contagem = int()

    # Início variáveis
    maior_por = 0
    menor_por = 999

    n = int(input())

    #Processamento
    for turma in range(1,n+1):
        id_turma = str(input())
        quant_matr = int(input())
        for aluno in range(1,quant_matr+1):
            matr_al = str(input())
            frequencia = str(input())
            if frequencia == "A":
                ausencias += 1
        porcent_ausen = (ausencias*100)/quant_matr
        ausencias = 0

        if porcent_ausen > maior_por:
            maior_por = porcent_ausen
            turma_maior = id_turma

        if porcent_ausen < menor_por:
            menor_por = porcent_ausen
            turma_menor = id_turma

        if porcent_ausen > 20:
            contagem += 1

        print(f"TURMA={id_turma} AUSENCIA={porcent_ausen:.2f}%")
    print(f"TURMA COM MAIOR PORCENTAGEM DE AUSENCIA={turma_maior} AUSENCIA={maior_por:.2f}%")
    print(f"TURMA COM MENOR PORCENTAGEM DE AUSENCIA={turma_menor} AUSENCIA={menor_por:.2f}%")
    print(f"{contagem} TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%")





if __name__ == "__main__":
    main()