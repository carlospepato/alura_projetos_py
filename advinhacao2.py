import random


def jogar():

    print("************************")
    print("Bem vindo ao jogo de advinhação 2.0")
    print("************************")

    # random sempre cria numeros de 0.0 a 1.0
    numero_secreto = round(random.randrange(1, 101))
    rodada = 1
    tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade você quer escolher:')
    print('(1) Fácil\n(2) Médio\n(3) Díficil')

    nivel = int(input(''))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou', chute)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Parabens! Você acertou e fez {} pontos.'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi maior que o número secreto')

            elif(menor):
                print('Você Errou! O seu chute foi menor que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim de jogo')
    print('O número secreto é : {}'.format(numero_secreto))


if(__name__ == "__main__"):
    jogar()
