# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor que estão na tupla.

import random

n = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
     random.randint(0, 10), random.randint(0, 10))


print(f'Menor número gerado {min(n)} \nMaior número gerado : {max(n)}')
