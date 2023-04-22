# Exercício Python 009 : Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número qualquer : '))
for i in range(1, 10 + 1):
    print(f'{n} x {i} = {n * i}')
# Não era pra ser usado estrutura de repetição, porém eu estava com preguiça de escrever o mesmo código 10x.
