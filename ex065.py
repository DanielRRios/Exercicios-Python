# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

lts = []
total = 1
n = int(input('Digite um número : '))
lts.append(n)
while True:
    cont = input('Deseja continuar? [s / n] : ')
    if(cont != 'n'):
        n = int(input('Digite qualquer número : '))
        lts.append(n)
        total += 1 
    else:
        break

print(f'Menor valor {min(lts)} - Maior valor {max(lts)} - Total {total}')
    
    
