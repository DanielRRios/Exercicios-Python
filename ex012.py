# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('Valor do produto : '))
desc = prod * 95 / 100
print(f'O produto que custava R${prod:.2f}, na promoção com desconto de 5% vai custar R${desc:.2f}')
