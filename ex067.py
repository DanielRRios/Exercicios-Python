# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.

while True:
    n = int(input('Digite um número : '))
    if(n <= 0):
        break
    else:
        cont = 1
        while(cont <= 10):
            print(f'{n} x {cont} = {n * cont}')
            cont += 1
