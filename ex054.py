# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são maiores.

lts = []
maior = menor = 0
for i in range(1, 8):
    n = int(input(f'Digite o ano de nascimento da {i}° pessoa : '))
    ano = 2023 - n
    lts.append(ano)

for i in lts:
    if i >= 18:
        maior += 1
    else:
        menor += 1

print(f'Total de maiores : {maior} \nTotal de menores : {menor}')
