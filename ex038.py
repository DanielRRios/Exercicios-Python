# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número : '))
n2 = int(input('Segundo número : '))
if(n1 > n2):
    print(f'O primeiro número digitado é maior')
elif(n2 > n1):
    print(f'O Segundo número digitado é maior')
else:
    print(f'Os dois números são iguais.')
