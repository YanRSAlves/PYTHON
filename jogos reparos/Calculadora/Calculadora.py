print('''                                     
              **CALCULADORA**

  ________________________________   
 |     Escolha um operador abaixo |
 | 1 - ADIÇÃO                     |
 | 2 - SUBTRAÇÃO                  |
 | 3 - MULTIPLICAÇÃO              |
 | 4 - DIVISÃO                    |
 | 5 - POTENCIA                   |
 | 6 - PORCENTAGEM                |
 |________________________________|

''')
escolha = input('Selecione um operador:  ')

  #ADIÇÃO
if escolha == '1':
    soma_1 = float(input('Digite o primeiro numero:  '))
    soma_2 = float(input('Digite o segundo numero:  '))
    soma_3 = (soma_1+soma_2)
    print('Seu resultado é: {}' .format(soma_3))
    
  #SUBTRAÇÃO
elif escolha == '2':
    subtração_1 = float(input('Digite o primeiro numero:  '))
    subtração_2 = float(input('Digite o segundo numero:  '))
    subtração_3 = (subtração_1-subtração_2)
    print('Seu resultado é: {}' .format(subtração_3))

  #MULTIPLICAÇÃO
elif escolha == '3':
    multiplicação_1 = float(input('Digite o primeiro numero:  '))
    multiplicação_2 = float(input('Digite o segundo numero:  '))
    multiplicação_3 = (multiplicação_1*multiplicação_2)
    print ('Seu resultado é: {}' .format(multiplicação_3))

  #DIVISÃO
elif escolha == '4':
    divisão_1 = float(input('Digite o primeiro numero:  '))
    divisão_2 = float(input('Digite o segundo numero:  '))
    divisão_3 = (divisão_1/divisão_2)
    print ('Seu resultado é: {}' .format(divisão_3))

  #POTENCIA
elif escolha == '5':
    potencia_1 = float(input('Digite o primeiro número:  '))
    potencia_2 = float(input('Digite o segundo número:  '))
    potencia_3 = (potencia_1**potencia_2)
    print('Seu resultado é: {}'.format(potencia_3))

  #PORCENTAGEM
elif escolha == '6':
    porcentagem_1 = float(input('Digite o primeiro numero:  '))
    porcentagem_2 = float(input('Digite o segundo numero:  '))
    porcentagem_3 = (porcentagem_1+porcentagem_2)
    print('Seu resultado é: {}' .format(porcentagem_3))

  #ERRO
else:
    print ('você não digitou um operador válido, tente novamente')
