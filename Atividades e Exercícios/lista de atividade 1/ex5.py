#5) QUESTAO:
filmes = ['Thor', 'Homem de ferro', 'Vingadores Ultimato', 'Pantera Negra','Capitao América','Doutor Estranho', 'Guardiões da Galaxia', 'Homem Formiga e a Vespa','Capitã Marvel','Incrivel Hulk']
print(filmes)
print()
filmes.remove('Homem Formiga e a Vespa')
print(filmes)
print()
filmes = filmes +['Deadpool']
print(filmes)
print()
filmes.remove('Doutor Estranho')
filmes.remove('Homem de ferro')
print(filmes)
print()
print('total de posições é ',len(filmes))
print('a sua posicão hulk é ',filmes.index('Incrivel Hulk'))
print('o tamanho lista é',len(filmes))
