#QUESTÃO 2

contas = {'Poliano Habla': 12, 'Roberto Advogado': 2, 'Ana Eu': 100000, 'Leo Parker': 5, 'Adryan Careca': 3}
conta = str(input("\nDigite o nome do cliente: ")).title().strip()

valor = {contas.get(conta)}

print(f'Valor da conta: {valor}')
print(f'Quantidade de digitos: {len(str(valor))-2}')
