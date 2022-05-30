import random


def jogar():
    imprimi_mensagem_inicio()
    palavra_secreta = pega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    dica = "Fruta"
    print(f'******** Dica: {dica.upper()} ********')
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            mensagem_enforcou(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        exibe_resultado(acertou, enforcou, palavra_secreta)

    print("Fim do jogo")


def imprimi_mensagem_inicio():
    separador = "*********************************"
    print(separador)
    print("Bem vindo ao jogo da Forca")
    print(separador)


def pega_palavra_secreta():
    palavras = []
    arquivo = open('palavras.txt', 'r')

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def marca_chute_correto(palavra, chute, letras):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras[index] = letra
        index += 1


def exibe_resultado(acertou, enforcou, palavra):
    if acertou:
        return print("Parabéns você acertou a palavra.")
    elif enforcou:
        return print(f"Você se tornou uma lastima da sociedade. A palavra era: {palavra.lower()}.")


def mensagem_enforcou(erros):
    if erros == 1:
        print("   _________   ")
        print("  |/        |  ")
        print("  |       (x-x) ")
        print("  |            ")
        print("  |            ")
        print("__|__          ")

    if erros == 2:
        print("   _________   ")
        print("  |/        |  ")
        print("  |       (x-x) ")
        print("  |         |  ")
        print("  |            ")
        print("__|__          ")

    if erros == 3:
        print("   _________   ")
        print("  |/        |  ")
        print("  |       (x-x) ")
        print("  |        /|  ")
        print("  |            ")
        print("__|__          ")

    if erros == 4:
        print("   _________   ")
        print("  |/        |  ")
        print("  |       (x-x) ")
        print("  |        /|\ ")
        print("  |            ")
        print("__|__          ")

    if erros == 5:
        print("   _________   ")
        print("  |/        |  ")
        print("  |       (x-x) ")
        print("  |        /|\ ")
        print("  |        /   ")
        print("__|__          ")

    if erros == 6:
        print("   _________   ")
        print("  |/        |  ")
        print("  |       (x-x) ")
        print("  |        /|\ ")
        print("  |        / \ ")
        print("__|__          ")


if __name__ == "__main__":
    jogar()
