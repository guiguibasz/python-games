import random as rd
from os import system

def jogar():

    abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while not acertou and not enforcou:

        chute = pede_chute()

        if chute in palavra_secreta:
            chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)



#                      *******************************
#                      *********   FUNÇÕES   *********
#                      *******************************



def abertura():
    print('************************************')
    print('** Bem vindo(a) ao Jogo da Forca! **')
    print('************************************')

def carrega_palavra_secreta():
    print('Qual modo de jogo você deseja jogar?')
    tipo_de_jogo = int(input('(1) Frutas (2) Estados (Brasileiros): '))
    if tipo_de_jogo == 1:
        arquivo_frutas = open("frutas.txt", "r")
        frutas = []

        for linha in arquivo_frutas:
            linha = linha.strip()
            frutas.append(linha)

        arquivo_frutas.close()
        numero = rd.randrange(0, len(frutas))
        palavra_secreta = frutas[numero].upper()

    elif tipo_de_jogo == 2:
        arquivo_estados = open("estados.txt", "r")
        estados = []

        for linha in arquivo_estados:
            linha = linha.strip()
            estados.append(linha)

        arquivo_estados.close()
        numero = rd.randrange(0, len(estados))
        palavra_secreta = estados[numero].upper()
    else:
        print("Escolha entre 1 e 2...")

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input('Qual letra? ').strip().upper()
    while True:
        # método isalpha está verificando se tem caracteres diferente de letras
        if len(chute) != 1 or chute.isalpha() == False:
            system('cls||clear')
            print('NÃO É PERMITIDO:\n- MAIS DE UM DIGITO;\n- DIGITOS ESPECIAIS;\n- NÚMEROS OU ESPAÇOS.')
            print('\nTENTE NOVAMENTE!!!')
            chute = input('\nDigite uma letra: ').upper().strip()
            continue
        else:
            system('cls||clear')
            break
    return chute

def chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == "__main__":
    jogar()
