# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

nuns = []
for i in range(1, 4):
    n = int(input(f'Informe o {i}° número : '))
    nuns.append(n)

print(f'Menor {min(nuns)} - Maior {max(nuns)}')
