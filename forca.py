def jogar():
    separador = "*********************************"
    print(separador)
    print("Bem vindo ao jogo da Forca")
    print(separador)

    palavra_secreta = "alface".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        exibe_resultado(acertou, enforcou)

    print("Fim do jogo")


def exibe_resultado(acertou, enforcou):
    if acertou:
        return print("Parabéns você acertou a palavra")
    elif enforcou:
        return print("Você se tornou uma lastima da sociedade.")


if __name__ == "__main__":
    jogar()
