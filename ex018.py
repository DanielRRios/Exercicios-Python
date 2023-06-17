# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


import math
n1 = int(input('Digite um numero : '))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tag = math.tan(math.radians(n1))
print(f'O Ângulo de {n1} tem o SENO de {sen:.2f}, COSSENO {cos:.2f}, TANGENTE {tag:.2f}')
