# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('Informe o primeiro termo : '))
ra = int(input('Informe a razão : '))
cont = 0
for i in range(pt, pt * pt, ra):
    print(f'{i}')
    if(cont == 10):
        break
    cont += 1
    
