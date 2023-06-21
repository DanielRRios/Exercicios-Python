# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Informe o primeiro número : '))
n2 = int(input('Informe o segundo número : '))
while True:
    op = int(input(f'[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \nEscolha uma opção : '))
    if(op == 1):
        print(f'A soma entre {n1} + {n2} = {n1 + n2} \n')
    elif(op == 2):
         print(f'A nultiplicação entre {n1} x {n2} = {n1 * n2} \n')   
    elif(op == 3):
        if(n1 > n2):
            print(f'O primeiro número é maior \n')
        elif(n2 > n1):
            print(f'O segundo número é maior \n')
        else:
            print(f'Os dois números digitados são iguais \n')
    elif(op == 4):
        n1 = int(input('Informe o primeiro número : '))
        n2 = int(input('Informe o segundo número : '))
    elif(op == 5):
        print(f'Obrigado por utilizar nosso programa! \n')
        break
    else:
        print(f'{op} NÃO É UMA OPÇÃO VALIDA! \n')
