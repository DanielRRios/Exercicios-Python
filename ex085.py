# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

nuns = [], []
for i in range(1, 8):
    n = int(input(f'Informe o {i}° valor : '))
    if(n % 2 == 0):
        nuns[0].append(n)
    else:
        nuns[1].append(n)

print(sorted(nuns[0]))
print(sorted(nuns[1]))
