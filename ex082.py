# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lts = []
par = []
impar = []
while True:
    n = int(input('Digite qualquer número (0 para parar) : '))
    if(n == 0):
        break
    if(n % 2 == 0):
        lts.append(n)
        par.append(n)
    else:
        lts.append(n)
        impar.append(n)

print(f'Todos números : {lts} \nPares : {par} \nImpares : {impar}')
    
