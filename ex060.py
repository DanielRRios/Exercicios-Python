# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

total = 1
n = int(input('Informe um número qualquer : '))
for i in range(1, n + 1):
    total *= i

print(f'Fatorial de {n} = {total}')
