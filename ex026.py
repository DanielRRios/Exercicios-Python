# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a
# primeira vez e em que posição ela aparece a última vez.

fr = input('Digite uma frase : ')

um = fr.index('a')
ult = fr.rindex('a')
print(f'Primeira posição {um + 1}, ultima posição {ult + 1}')
