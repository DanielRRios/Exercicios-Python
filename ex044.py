# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

vl = float(input('Valor do produto : '))
op = int(input('Modos de pagamento \n[1] À vista \n[2] À vista cartão \n[3] 2x Cartão \n[4] 3x ou mais \nModo de pagamento : '))

if(op == 1):
    print(f'Você ganhou 10% de desconto na sua compra de {vl}, novo valor do produto R${vl * 90 / 100}')
elif(op == 2):
    print(f'Você ganhou 5% de desconto na sua compra de {vl}, novo valor do produto R${vl * 95 / 100}')
elif(op == 3):
    print(f'O pagamento deve ser feito em duas vezes de R${vl / 2:.2f}')
elif(op == 4):
    parc = int(input('Em quantas vezes deseja parcelar : '))
    pag = vl * 120 / 100
    print(f'O pagamento deve ser feito em {parc} vezes de R${pag / parc:.2f}')
else:
    print(f'{op} não é uma opção valida')
