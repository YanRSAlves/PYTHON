
#4) QUESTAO:
pedido = []
lista = ['tomate','ovo','sal', 'doce','fria']

print('Faça um upgrade na sua pizza escolhida\n')
print('Adicione ate 5 adicionais gratuitos')
print(lista)


y = int(input('quantos ingredientes a mais vai querer: '))
for x in range (0,y):
    adicional = str(input(f'adicione {y} ingredientes '))
    pedido.append(adicional)

print('\n\nos adicioanis que voce escolheu foi = ',pedido)

