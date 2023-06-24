# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de
# inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

lista = []
num = int(input("Digite o número de elementos na lista: "))

for i in range(num):
    n = int(input("Digite um número: "))
    lista.append(n)

for i in range(len(lista)):
    indice_minimo = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[indice_minimo]:
            indice_minimo = j
    lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

print("Lista ordenada:", lista)

