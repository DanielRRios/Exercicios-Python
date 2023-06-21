# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

pt = int(input('Informe o primeiro termo da PA : '))
ra = int(input('Informe a razão da PA : '))

cont = 1
while(cont <= 10):
    if(cont == 1):
        print(pt)
    else:
        pt += ra
        print(pt)
    cont += 1
