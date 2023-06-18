# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao
# serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Ano de nascimento : '))
idade = 2023 - ano
if(idade < 18):
    print(f'Você ainda tem {idade} anos não pode se alistar, faltam {18 - idade} anos')
elif(idade > 18):
    print(f'Você está atrasado para se alistar, você passou {idade - 18} anos do prazo')
else:
    print(f'Você já pode se alistar, procure o quartel mais proximo')
