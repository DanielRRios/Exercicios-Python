# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Informe um número : '))
cont = 0

for i in range(2, n + 1):
    if(n % i == 0):
        cont += 1

if(cont <= 2):
    print(f'PRIMO')
else:
    print(f'NÃO PRIMO')
