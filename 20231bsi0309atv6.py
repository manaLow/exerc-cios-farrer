#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20231bsi0309N.py atividade 6
#  
#  Copyright 2020 Manuely Meireles Lemos
#  

def main():
    
    #Declaração de variáveis
    quociente = int()
    num1 = float()
    num2 = float()
    div =  float()

    # Entrada de dados e inicio de variáveis 
    num1 = float(input())
    num2 = float(input())

    quociente = 0

    # Processamento
    if num1 > 0 and num2 > 0:
        while num1>=num2:
            num1 -= num2
            quociente += 1

        # Saída
        print(f'QUOCIENTE={quociente}')
    else:
        print("ENTRADA INVALIDA")

    


if __name__ == "__main__":
    main()