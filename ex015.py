# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias de aluguel? : '))
kms = float(input('Quantos Kms rodados? : '))
total = (dias * 60) + (kms * 0.15)
print(f'O total a pagar é de R${total:.2f}')
