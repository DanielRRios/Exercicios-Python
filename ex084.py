# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

peso = []
while True:
    p = float(input('Informe um peso (0 para parar) : '))
    if p == 0:
        break
    peso.append(p)
peso.sort()
maior = len(peso) - 2
print(f'{len(peso)} pesos cadastrados \nMais leves cadastrados {peso[0:2]}  \nMais pesados cadastrados {peso[maior:]}')
