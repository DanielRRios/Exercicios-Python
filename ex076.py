# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem
# de preços, organizando os dados em forma tabular.

prod = ('lapis', 2, 'caderno', 30, 'tesoura', 5, 'notebook', 2500)

for i in range(0, len(prod), 2):
    print(f'{prod[i]} {prod[i + 1]}')
