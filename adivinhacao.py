import random


def jogar():
    separador = "*********************************"
    print(separador)
    print("Bem vindo ao jogo de adivinhação!")
    print(separador)

    numero_secreto = random.randrange(1, 101)
    # print(numero_secreto)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("[1] Fácil | [2] Medio | [3] Difícil ")
    dificuldade = int(input("Digite a dificuldade: "))

    if dificuldade == 1:
        total_de_tentativas = 20
    elif dificuldade == 2:
        total_de_tentativas = 10
    elif dificuldade == 3:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(separador)
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = input("Digite um numero entre 1 e 100: ")
        print("Você digitou: ", chute)

        numero = int(chute)
        if numero < 1 or numero > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == numero
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if maior:
                print("Você errou e seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou e seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")
