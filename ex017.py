# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


co = float(input('Digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
hip = (co ** 2) + (ca ** 2)

print(f'A hipotenuza de {co} + {ca} é igual a {hip ** 0.5:.2f}')
