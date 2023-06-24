# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e
# as suas respectivas posições na lista.

lts = []
for i in range(1, 6):
    n = int(input(f'Digite o {i}° valor : '))
    lts.append(n)

print(f'Menor valor digitado {min(lts)} na posição {lts.index(min(lts))} \nMaior valor digitado {max(lts)} na posição {lts.index(max(lts))}')
