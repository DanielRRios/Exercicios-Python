# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vlCasa = float(input('Valor da casa : '))
vlSala = float(input('Qual seu salário : '))
qtdAno = int(input('Quantos anos vai pagar : '))

parcela = vlCasa / (qtdAno * 12)  
sal = vlSala * 30 / 100

print(f'Para pagar a casa de R${vlCasa} em {qtdAno} anos, a prestação será de R${parcela:.2f}')
if(sal < parcela):
    print('Seu empréstimo foi NEGADO')
else:
    print('Seu empréstimo foi APROVADO')
