# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


import random

total = 0
al = random.randint(1, 20)
chute = int(input('Chute um número de 1 a 20 : '))
while True:
    if(chute == al):
        total += 1
        break
    elif(chute < al):
        chute = int(input('Chute um número maior : '))
        total += 1
    elif(chute > al):
        chute = int(input('Chute um número menor : '))
        total += 1
print(f'O jogo acabou, você venceu em {total} tentativas!')
