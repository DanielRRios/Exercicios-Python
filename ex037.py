# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro : '))
esc = int(input('Escolha uma das bases para conversão \n[1] - BINARIO \n[2] - OCTAL \n[3] - HEXADECIMAL \nSua opção : '))


if(esc == 1):
    print(f'{num} convertido em BINARIO {bin(num)}')
elif(esc == 2):
    print(f'{num} convertido em OCTA {oct(num)}')
elif(esc == 3):
    print(f'{num} convertido em HEXADECIMAL {hex(num)}')
else:
    print(f'{esc} não é uma opção valida')
