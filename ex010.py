# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

md = float(input('Qual o valor que você tem na carteira? '))
dolar = md / 5.05
euro = md / 5.60

print(f'Com R${md} você pode comprar \n${dolar:.2f} Dólares \n${euro:.2f} Euros')
