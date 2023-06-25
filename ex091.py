# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No
# final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


import random

teste = {
}
for i in range(1, 5):
    n = random.randint(1, 10)
    teste['jogador' + str(i)] = n

x = dict(sorted(teste.items(), key=lambda x:x[1]))
for i, v in x.items():
    print(i, v)
