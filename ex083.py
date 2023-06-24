# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.

ex = input('Digite uma expressão : ')
e = ex.count('(')
d = ex.count(')')
if(e == d):
    print(f'É uma expressão válida!')
else:
    print(f'Não é uma expressão válida!')
