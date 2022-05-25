import forca
import adivinhacao

separador = "*********************************"

print(separador)
print("******* Escolha seu jogo! *******")
print(separador)

print("[1] Adivinhação | [2] Forca")
resultado = int(input("Qual o jogo desejado: "))

if resultado == 1:
    print("Jogando Adivinhação")
    adivinhacao.jogar_adivinhacao()
elif resultado == 2:
    print("Jogando Forca")
    forca.jogo_forca()
