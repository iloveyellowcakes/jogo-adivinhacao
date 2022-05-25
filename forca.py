def jogar():
    separador = "*********************************"
    print(separador)
    print("Bem vindo ao jogo da Forca")
    print(separador)

    palavra_secreta = "banana"
    enforcou = False
    nao_enforcou = False

    while not enforcou and not nao_enforcou:
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.lower() == letra:
                print(f"Encontrei a letra {chute} em posição {index}")
            index = index + 1
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
