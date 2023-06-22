# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

campeonato = ['corinthians', 'palmeiras', 'são paulo', 'santos', 'chapecoense',
              'flamengo', 'vasco', 'botafofo', 'fluminense', 'vitoria',
              'gremio', 'internacional', 'cuiaba', 'bahia', 'cruzeiro',
              'atletico', 'fortaleza', 'ponte', 'goias', 'bragantino']

print(f'5 Primeiros : {campeonato[0:5]} \n4 Ultimos colocados : {campeonato[-4:]} \n{sorted(campeonato)} \nA chapecoense está na {campeonato.index("chapecoense") + 1}° posição')
