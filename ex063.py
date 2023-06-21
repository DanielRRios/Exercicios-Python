# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

num = int(input('Digite a quantidade de números: '))
n1 = fib = cont = 0
n2 = 1

if num <= 0:
    print('Número inválido')
elif num == 1:
    print('0')
elif num == 2:
    print('0 → 1', end='')
else:
    print('0 → 1', end='')
    while cont < (num - 2):
        fib = n1 + n2
        print(f' → {fib}', end='')
        n1 = n2
        n2 = fib
        cont += 1
