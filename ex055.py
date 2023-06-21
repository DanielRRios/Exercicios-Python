# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = []
for i in range(1, 6):
    n = int(input(f'Peso da {i}° pessoa : '))
    peso.append(n)

print(f'Menor peso registrado : {min(peso)} \nMaior peso registrado : {max(peso)}')
