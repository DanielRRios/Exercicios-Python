# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"Notas de 50 - {nota50} \nNotas de 20 - {nota20} \nNotas de 10 - {nota10} \nNotas de 1 - {nota1}")
