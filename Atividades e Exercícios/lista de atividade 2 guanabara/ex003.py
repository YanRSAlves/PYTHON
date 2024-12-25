#SOMA DE DOIS NUMEROS
print('ALGORITMO DA SOMA DE DOIS NÚMEROS INTEIROS AND REAIS!\n')
number1i = int(input('Informe number1 inteiro: '))
number2i = int(input('Informe number2 inteiro: '))

somai = number1i + number2i

print('A soma dos numeros inteiros é igual a: ', somai)
print('A soma vale {}'.format(somai))
print('A soma entre os inteiros {0} e {1} vale {2}'.format(number1i,number2i,somai))

number1f = float(input('\nInforme number1 real: '))
number2f = float(input('Informe number2 real: '))

somaf = number1f + number2f
print('A soma dos numeros reais é igual a: ', somaf)
print('A soma entre os numeros reais {0} e {1} vale {2:.3f}'.format(number1f,number2f,somaf))