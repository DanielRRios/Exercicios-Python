# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o
# nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idades = []
hm = ''
idade = 1
ml = 0
for i in range(1, 5):
    n = input('Nome : ')
    i = int(input('Idade : '))
    s = input('Sexo [m / f] : ')
    idades.append(i)
    for i in idades:
        if(s == 'm'):
            if(i > idade):
                idade = i
                hm = n
    if(s == 'f' and i >= 20):
        ml += 1
print(f'A média das idades é {sum(idades) / len(idades)} \nO homem mais velho é {hm} com {idade} anos \nExistem {ml} mulheres com mais de 20 anos ')

    
