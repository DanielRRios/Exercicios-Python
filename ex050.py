# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

lts = []
for i in range(1, 7):
    n = int(input(f'Informe o {i}° número : '))
    lts.append(n)

soma = 0
for i in lts:
    if i % 2 == 0:
        soma += i
print(f'A soma dos pares é {soma}')
