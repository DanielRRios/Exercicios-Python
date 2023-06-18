# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'As retas {r1}, {r2}, e {r3} PODEM formar um triângulo') 
else:
    print(f'As retas {r1}, {r2}, e {r3} {decisão} não PODEM formar um triângulo') 
