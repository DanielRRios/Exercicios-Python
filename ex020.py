# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random 

n1 = input('Primeiro aluno : ')
n2 = input('Segundo aluno : ')
n3 = input('Terceiro aluno : ')
n4 = input('Quarto aluno : ')
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print(alunos)



