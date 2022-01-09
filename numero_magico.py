import random as rd

def jogar():
    print('********************')
    print('Jogo da Adivinhação!')
    print('********************')

    numeroSecreto = int(rd.randrange(1,101))
    totalDeTentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        totalDeTentativas = 20
    elif (nivel == 2):
        totalDeTentativas = 10
    else:
        totalDeTentativas = 5


    for rodada in range(1, totalDeTentativas + 1):
        print(f'---------------------------------------------------------- \n \t \t tentativa {rodada} de {totalDeTentativas}')
        chute = int(input('Digite o seu chute entre 1 e 100: '))
        print(f'\n Você chutou: {chute}')

        if chute <= 1 or chute >= 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = numeroSecreto == chute
        maior = numeroSecreto < chute
        menor = numeroSecreto > chute

        if acertou:
            print(f'\n Você acertou e fez {pontos} ! Parabéns!!')
            break

        else:
            if menor:
                print(f'\n O seu chute foi menor que o número secreto.')

            elif(maior):
                print(f'\n O seu chute foi maior que o número secreto.')

            pontos_perdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontos_perdidos

    print(f'O número secreto era {numeroSecreto}. Você fez {pontos}')

    print(f'\n \t  Fim do jogo!')

if __name__ == "__main__":
    jogar()