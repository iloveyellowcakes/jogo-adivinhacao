﻿import adivinhacao
import forca


def escolha_jogo():
    separador = "*********************************"
    print(separador)
    print("******* Escolha seu jogo! *******")
    print(separador)

    print("[1] Adivinhação | [2] Forca")
    resultado = int(input("Qual o jogo desejado: "))

    if resultado == 1:
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif resultado == 2:
        print("Jogando Forca")
        forca.jogar()


if __name__ == "__main__":
    escolha_jogo()
