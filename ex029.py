# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input("Quantos Km's por hora? "))
if(vel > 80):
    multa = vel - 80
    print(f'Você foi multado, valor a ser pago R${multa * 7:.2f}')
else:
    print(f'Tenha um bom dia, dirija com segurança!')
    
