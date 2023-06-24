# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela
# com a formatação correta.

mt = [[], [], []], [[], [], []], [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input('Digite um valor : '))
        mt[i][j] = n

for i in mt:
    print(i)
