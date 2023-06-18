# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Informe seu salário : '))
if(sal <= 1250):
    print(f'Seu salário com reajuste de 15% é R${sal * 115 / 100:.2f}')
else:
    print(f'Seu salário com reajuste de 10% é R${sal * 110 / 100:.2f}')
