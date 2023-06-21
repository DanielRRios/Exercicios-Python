# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pt
c = 2
extra = int(input('Indique a quantidade de termos que deseja visualizar: '))
h = 1
print(f'PA: {pt}')
while h != 0:
    extra += h
    while c <= extra:
        c += 1
        termo += r
        print(termo)
    h = int(input('\nQuantos termos você quer mostrar a mais? [0 para parar]'))
print(f'\nProgressão finalizada com {c-2} termos mostrados.')
