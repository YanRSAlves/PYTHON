aposta = 'S'
valorApostado = 0

while aposta == 'S':
    n = float(input('Informe o valor da aposta: '))
    aposta = input('quer continuar apostando? [S/N]: ').upper()
    valorApostado += n

print(f'\nMuito obrigado pelas apostas no total de R${valorApostado}! ')
print('Verifique seus ganhos na bilheteria!\n')