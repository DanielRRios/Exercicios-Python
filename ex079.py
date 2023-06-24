# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele
# não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lts = []
while True:
    n = int(input('\nDigite um valor inteiro : '))
    if(n not in lts):
        lts.append(n)
    else:
        print(f'Valor já inserido, por favor digite outro\n')

    c = input('Deseja continuar? [s / n] : ').lower()
    if(c == 'n'):
        break

print(f'A lista de números cadastrados foi : {sorted(lts)}')
