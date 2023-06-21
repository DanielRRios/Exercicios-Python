# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de
# parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

lts = []
while True:
    n = int(input('Digite um número : '))
    if(n == 999):
        break
    else:
        lts.append(n)

print(f'A soma dos {len(lts)} valores é {sum(lts)}')
