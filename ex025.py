#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

n = input('Informe seu nome completo : ').lower()
nome = n.split()

print(f'Seu nome tem silva? ', 'silva' in nome)
