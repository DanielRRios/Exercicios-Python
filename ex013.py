# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Seu sálario atual : '))
novo = sal * 115 / 100
print(f'Com o aumento de 15% seu sálario passa a ser R${novo:.2f}')
