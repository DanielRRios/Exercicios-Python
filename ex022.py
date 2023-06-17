#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

n = input('Diite seu nome completo : ')
print(n.upper())
print(n.lower())
x = n.replace(' ', '')
print(len(x))
d = n.split()
print(len(d[0]))
