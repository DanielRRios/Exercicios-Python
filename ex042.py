# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 > r2 - r3 and r2 > r1 - r3 and r3 > r2 - r1:
    if (r1 == r2 and r1 == r3 and r2 == r3):
        print("É possível criar um triângulo equilátero")
    elif (r1 != r2 and r1 != r3 and r2 != r3):
        print("É possível criar um triângulo escaleno")
    else:
        print("É possível criar um triángulo isóceles")
else:
    print("Não é possível formar um triangulo!") 
