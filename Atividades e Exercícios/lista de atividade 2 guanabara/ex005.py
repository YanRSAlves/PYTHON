valor = input('Digite um valor: ')
print('Esse valor pode ser numérico? ',valor.isnumeric())
print('Esse valor pode ser alfabético? ',valor.isalpha())
print('Esse valor é alfabético e numérico? ', valor.isalnum())

string = input('Digite um texto: ')
print('Esse texto está todo em MAÍUSCULO? ', string.isupper())