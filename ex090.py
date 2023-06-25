# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da
# estrutura na tela.

nota = {
    
}

n = input('Nome do aluno : ')
m = float(input('Média do aluno : '))

if(m < 5):
    s = 'Reprovado'
elif(m >= 5 and m <=7):
    s = 'Recuperação'
else:
    s = 'Aprovado'

nota['nome'] = n
nota['media'] = m
nota['situacao'] = s

print(f'- Nome : {nota["nome"]} \n- Média : {nota["media"]} \n- Status : {nota["situacao"]}')
