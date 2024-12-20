# print('Hello word')

# Variáveis

# nome_usuario = 'Yan Rocha'  # String de 9 caracteres
# print(nome_usuario)
#
# name, idade = 'Yan', 18
# nota1 = nota2 = nota3 = 10.5
# media = 7
# estado = False
#
# #Função type()
# print(type(nome_usuario))
# print(type(media))
# print(type(nota1))
# print(type(estado))
# print(type(type(8)))
# print(type(1+2j))

#Função isinstance()
# a = 10
# b = 'Sol'
# print(isinstance(b, (int, float)))
# def teste_type(valor):
#     if (isinstance(valor, float)) == True:
#         print('Valor Float')
#     else:
#         print('Valor Integer')
# dado = 7.5
# teste_type(dado)
# OPERADOR OPERAÇÃO
# +   SOMA
# -   SUBTRAÇÃO
# *   MULTIPLICAÇÃO
# /   DIVISÃO REAL
# //  DIVISÃO INTEIRA (SOBRA)
# %   MODULAÇÃO(MOD)
# **  POTÊNCIAÇÃO

#ORDEM DE PRECEDÊNCIA DOS OPERADORES
#PARÊNTESES
#POTÊNCIAÇÃO
#MULTIPLICAÇÃO/DIVISÃO
#SOMA/SUBTRAÇÃO
#ESQUERDA PARA DIREITA

# idade = 15
# altura = 1.75
#
# resultado = (idade >= 18) and (altura >= 1.70)
# msg = 'Pode participar do evento? ' + str(resultado)
#
# print(msg)

#PROGRAMA DE DISPARO DE ALARME
#
# porta = 'a'
# janela = 'f'
#
# alarme = (porta == 'a') or (janela == 'a')
# msg = 'Alarme disparado? ' + str(alarme)
#
# print(msg)

# print('PROGRAMA DE AVALIÇÕES ESCOLARES')
# def lernotas():
#     nota=float(input('Digite uma nota para o aluno(a): '))
#     return nota
#
#
# def resultado(nota1,nota2):
#     media=(nota1+nota2)/2
#     print("Nota 1: ", nota1)
#     print("Nota 2: ",nota2)
#     print(f'Nota1 + Nota2 = {nota1+nota2} Dividido por 2 = {media}  ')
#     print("Média: ", media, "Resultado: ", end="")
#     if media >= 7:
#         print("Aprovado por Média ")
#         print('Parabéns! \nBoas Férias')
#     elif (media >= 4) and (media < 7):
#         print('Ficou de Recuperação')
#         recuperacao(media)
#     else:
#         print("Média Menor que 4 Reprovado! ", end='')
#         print('Estude mais!')
# def recuperacao(media):
#     print('Já fez a prova de recuperação? [s/n]')
#     option = input().upper()
#     if option == 'S':
#         nota_recuperacao = float(input('Qual foi sua                 -nota de Recuperação: '))
#         resultado(media, nota_recuperacao)
#     else:
#         print('Estude Para Prova Final!')
#
#
#
#
# a = lernotas()
# b = lernotas()
# resultado(a,b)

#EXERCÍCIOS BEECROWD:

#Neste problema, deve-se ler o código de uma peça 1,
# o número de peças 1, o valor unitário de cada peça 1,
# o código de uma peça 2, o número de peças 2 e o valor unitário
# de cada peça 2. Após, calcule e mostre o valor a ser pago.

# Entrada
# O arquivo de entrada contém duas linhas de dados.
# Em cada linha haverá 3 valores, respectivamente dois inteiros
# e um valor com 2 casas decimais.
#
# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo,
# lembrando de deixar um espaço após os dois pontos e um espaço após o "R$".
# O valor deverá ser apresentado com 2 casas após o ponto.

# peca1 = list(map(float, input().split()))
# peca2 = list(map(float, input().split()))
#
# total1 = peca1[1] * peca1[2]
# total2 = peca2[1] * peca2[2]
# total = total1 + total2
#
# print(f'VALOR A PAGAR: R$ {total:.2f}')



#
# pi = 3.14159
#
# Raio = float(input())
#
# volume = (4.0/3.0) * pi * (Raio**3)
#
# print(f'VOLUME = {volume:.3f}')




# valor = int(input())
#
# respostas = list(map(int, input().split()))
# acertos = respostas.count(valor)
# print(acertos)