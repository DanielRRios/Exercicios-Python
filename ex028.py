# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

ale = random.randint(1, 10)
n = int(input('Chute um numero de 1 a 10 : '))

if(ale == n):
    print(f'Acertou zé!')
else:
    print(f'Errou zé, o número certo era {ale}')
