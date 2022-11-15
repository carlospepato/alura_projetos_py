import time

import advinhacao2
import forca

print("************************")
print("****Escolha seu jogo****")
print("************************")

print('(1) Forca (2) Advinhação')

jogo = int(input('Qual o jogo:'))

if jogo == 1:
    trespontos = '.' + time.sleep(1) + '.' + time.sleep(1) + '.'
    print('Carregando o jogo da forca...')
    time.sleep(5)
    forca.jogar()
elif jogo == 2:
    print('Carregando o jogo da advinhação...')
    time.sleep(3)
    advinhacao2.jogar()
