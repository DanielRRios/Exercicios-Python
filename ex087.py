# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

mt = [[], [], []], [[], [], []], [[],[],[]]
t = 0

for t in range(0, 3):
    for u in range(0, 3):
        n = int(input('Informe um valores : '))
        mt[t][u] = n
    
for i in range(0, 3):
    for j in range(0, 3):
        if(mt[i][j] % 2 == 0):
            t += mt[i][j]
print('-' * 10)
for p in mt:
    print(p)
        
print('-' * 10)

print(f'A soma de todos os pares digitados : {t}')

a = (mt[0][2]) + (mt[1][2]) + (mt[2][2])
print(f'A soma das terceiras colunas : {a}')

sm = [mt[0][1], mt[1][1], mt[2][1]]
print(f' Maior número encontrado na segunda linha : {max(sm)}')


