# Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze'
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
n = int(input('Informe um número de 0 a 20 : '))
print(f'{n} escrito = {num[n]}')
