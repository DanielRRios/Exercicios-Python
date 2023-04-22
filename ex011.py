# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Qual a largura da sua parede? : '))
alt = float(input('Qual a altura da sua parede? : '))
area = larg * alt
print(f'Sua área é de {area:.2f}M² \nVocê vai precisar de {area / 2:.2f}L de tinta')
