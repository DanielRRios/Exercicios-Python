# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    n = int(input('informe um número : '))
    lista.append(n)

    cont = input(f'\nDeseja continuar? [S / N] : ').lower()
    if(cont == 'n'):
        break

if(5 in lista):
    x = 'Sim'
else:
    x = 'Não'
lista.sort()
print(f'{len(lista)} números digitados \n{list(reversed(lista))} \n5 existe na lista? {x}')
