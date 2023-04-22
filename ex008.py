# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

mt = int(input('Informe uma distância em metros : '))
print(f'A media de {mt}m corresponde a : \n{mt / 1000}Km \n{mt / 100}Hm \n{mt / 10}Dam')
print(f'{mt * 10}Dm \n{mt * 100}Cm \n{mt * 1000}mm')
