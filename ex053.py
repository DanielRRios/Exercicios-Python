# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

fr = input('Digite uma frase : ').replace(' ','')
pol = fr[::-1]
if(fr == pol):
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
