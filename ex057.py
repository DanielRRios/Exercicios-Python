# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até
# ter um valor correto.

while True:
    s = input('Informe seu sexo [M / F / O] : ').lower()
    if(s == 'm' or s == 'f' or s == 'o'):
        print('Sexo cadastrado com sucesso!')
        break
    else:
       print('Por favor informe uma opção valida!')
