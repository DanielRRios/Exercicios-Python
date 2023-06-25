# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
import time 
n = int(input('Quantos jogos deseja realizar? '))
for i in range(1,n+1):
    a = []
    for t in range(1, 7):
        ale = random.randint(1, 60)
        a.append(ale)
    if(a != None):
        print(f'{i}° jogo : {a}')
        time.sleep(1)
        
