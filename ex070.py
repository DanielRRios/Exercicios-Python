# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 


total = []
maior = 0

nm = input('Nome produto : ')
valor = float(input('Valor do produto : R$'))
total.append(valor)

preco = total[0]
prod = nm

while True:
    nm = input('\nNome produto : ')
    valor = float(input('Valor do produto : R$'))
    total.append(valor)

    if(valor < preco):
        preco = valor
        prod = nm

    if(valor >= 100):
        maior += 1

    cont = input('Deseja continuar? [s / n] : ')
    if(cont == 'n'):
        break

print(f'\nTotal gasto R${sum(total):.2f} \n{maior} produtos custam mais de R$ 100,00 \nO produto mais barato cadastrado foi {nm} custando R${preco:.2f}')
