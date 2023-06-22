# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de
# vitórias consecutivas que ele conquistou no final do jogo.

import random
vit = 0

while True:
    ale = random.randint(1, 9)
    esc = input('PAR OU IMPAR : ').lower()

    if(esc == 'par' and ale % 2 == 0):
        vit += 1
        print(f'\nParabéns, você venceu! ')
    elif(esc == 'impar' and ale % 2 == 1):
        vit += 1
        print(f'\nParabéns, você venceu! ')
    else:
        print(f'\nVocê perdeu! o resultado foi {ale} :( ')
        break
print(f'\nO jogo acabou, você venceu {vit} partidas!')
