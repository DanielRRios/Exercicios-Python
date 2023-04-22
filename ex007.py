# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Primeira nota do aluno : '))
n2 = float(input('Segunda nota do aluno : '))
media = (n1 + n2) / 2
print(f'A média entre {n1} + {n2} é igual a {media}')

# outra forma de executar o código sem a necessidade da variavel media
#print(f'A média entre {n1} + {n2} é igual a {(n1 + n2) / 2:.1f}')
