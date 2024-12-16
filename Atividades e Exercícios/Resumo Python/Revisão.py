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