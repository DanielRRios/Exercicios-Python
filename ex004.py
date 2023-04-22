# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

frase = input('Digite algo : ')
print(f'O tipo primitivo desse valor é {type(frase)}')
print(f'É um número? {frase.isnumeric()}')
print(f'É alfabetico {frase.isalpha()}')
print(f'É alfanumerico? {frase.isalnum()}')
print(f'Está em maiusculo? {frase.isupper()}')
print(f'Está em minusculo? {frase.islower()}')
print(f'Está capitalizada? {frase.istitle()}')
