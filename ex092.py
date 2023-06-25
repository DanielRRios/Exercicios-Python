# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for
# diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

dados = {}

dados['nome'] = input('Nome : ')
dados['nasc'] = int(input('Ano de nascimento : '))
dados['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['carteira'] == 0:
    print(f'-Nome : {dados["nome"]} \n-Ano de nascimento : {dados["nasc"]} \n-Ctps : {dados["carteira"]}')
else:
    dados['ano'] = int(input('Ano de contratação : '))
    dados['salario'] = float(input('Salario R$: '))
    dados['apo'] = 35 - (2023 - dados['ano']) + 2023 - dados['nasc']

    print(f'\n-Nome : {dados["nome"]} \n-Ano de nascimento : {dados["nasc"]} \n-Cps : {dados["carteira"]} \n-Contratação : {dados["ano"]}')
    print(f'-Sálario : {dados["salario"]:.2f} \n-Aposentadoria : {dados["apo"]}')
