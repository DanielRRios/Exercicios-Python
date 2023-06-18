# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

kms = float(input('Quantos kms de viagem? '))
if(kms <= 200):
    print(f'Você vai pagar R${kms * 0.50:.2f} na passagem')
else:
    print(f'Você vai pagar R${kms * 0.45:.2f} na passagem')
