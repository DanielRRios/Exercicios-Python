# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a
# média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

notas = []
cont = 0
while True:
    nome = input('Nome aluno : ')
    n1 = float(input('Primeira nota : '))
    n2 = float(input('Segunda nota : '))
    m = (n1 + n2) / 2

    aluno = {
        'nome' : nome,
        'nota1' : n1,
        'nota2' : n2,
        'media' : m
    }

    notas.append(aluno)

    cont = input('\nCadastrar mais alunos? [s / n] : ').lower()
    if(cont == 'n'):
        break
print(f'\n')
for c, e in enumerate(notas):
    print(c, notas[c]['nome'], notas[c]['media'])

while True:
    ver = int(input('\nDeseja ver as notas de qual aluno? (999 para parar) : '))
    if(ver == 999):
        break
    else:
        print(f'Nota 1 : {notas[ver]["nota1"]} - Nota 2 : {notas[ver]["nota2"]}')
