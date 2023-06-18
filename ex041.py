# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

ano = int(input('Seu ano de nascimento : '))
idade = 2023 - ano

if(idade <= 9):
    print(f'{idade} anos = Mirin')
elif(idade <= 14):
    print(f'{idade} anos = Infantil')
elif(idade <= 19):
    print(f'{idade} anos = Junior')
elif(idade <= 25):
    print(f'{idade} anos = Senior')
else:
    print(f'{idade} anos = Master')
