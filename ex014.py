# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em C° : '))
f = (c * 9/5) + 32
print(f'A temperatura convertida de C° para F° é {f:.1f}')

# Formula : (0 °C × 9/5) + 32 = 32 °F
