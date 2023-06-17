# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cid = input('Diite o nome da sua cidade : ')
x = cid.lower().split()
if(x[0] == 'santo'):
    print(True)
else:
    print(False)
