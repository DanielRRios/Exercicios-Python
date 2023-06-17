# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Informe um número inteiro : '))
if(num % 2 == 0):
    print(f'{num} é PAR')
else:
    print(f'{num} é IMPAR')
