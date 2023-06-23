# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

t = (int(input('Primeiro numero : ')), int(input('Segundo numero : ')), int(input('Terceiro numero : ')), int(input('Quarto numero : ')))
        
print(f'{t.count(9)}, {t.index(3) + 1} ')
for i in t:
    if(i % 2 == 0):
        print(f'Pares encontrados na lista - {i}', end = " ")
