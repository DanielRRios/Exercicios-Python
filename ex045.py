# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
op = int(input('[1] pedra \n[2] papel \n[3] Tesoura \nEscolha sua jogada : '))
comp = randint(1,3)

if(op == 1 and comp == 1):
    print(f'EMPATOU, ambos escolheram PEDRA')
elif(op == 1 and comp == 2):
    print(f'PERDEU, o computador jogou PAPEL')
elif(op == 1 and comp == 3):
    print(f'GANHOU, o computador jogou TESOURA')
elif(op == 2 and comp == 1):
    print(f'GANHOU, o computador jogou PEDRA')
elif(op == 2 and comp == 2):
    print(f'EMPATOU, ambos escolheram PAPEL')
elif(op == 2 and comp == 3):
    print(f'PERDEU, o computadir jogou TESOURA')
elif(op == 3 and comp == 1):
    print(f'PERDEU, o computador jogou PEDRA')
elif(op == 3 and comp == 2):
    print(f'GANHOU, o computador jogou PAPEL')
elif(op == 3 and comp == 3):
    print(f'EMPATOU, ambos escolheram TESOURA')
else:
    print(f'OPÇÃO INVALIDA')
