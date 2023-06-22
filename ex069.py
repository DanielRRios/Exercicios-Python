# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior = hm = ml = 0
while True:
    idade = int(input('Informe a idade : '))
    sexo = input('Informe o sexo [m / f]: ')
    if(idade >= 18):
        maior += 1
    if(sexo == 'm'):
        hm += 1
    if(sexo == 'f' and idade >= 20):
        ml += 1

    cont = input('\nDeseja cadastrar mais pessoas? [s/n] : ')
    if(cont == 'n'):
        break

print(f'Você cadastrou {maior} pessoas maiores de idade \nVocê cadastrou {hm} homens \nVocê cadastrou {ml} mulheres com mais de 20 anos')
