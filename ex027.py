# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = input('Digite seu nome completo : ').split()
print(f'primeiro nome : {n[0]} \nUltimo nome : {n[-1]}')


