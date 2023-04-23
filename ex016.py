# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

n = float(input('Informe um numero : '))
print(f'A parte inteira do número digitado é {trunc(n)}')

