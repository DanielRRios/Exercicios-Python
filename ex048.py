# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

num = 0
cont = 0
for i in range(0, 500):
     if i % 2 != 0 and i % 3 == 0:
        num += 1
        cont += i
print(num, cont)
