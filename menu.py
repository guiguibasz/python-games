import forca as fc
import adivinhacao as ad

print('***************************')
print('****Escolha o seu jogo!****')
print('***************************')

print('(1) Forca (2) Adivinhação')

jogo = int(input('Qual jogo? '))

if (jogo == 1):
    print('Jogando Forca! \n')
    fc.jogar()

elif (jogo == 2):
    print("Jogando Adivinhação! \n")
    ad.jogar()
    