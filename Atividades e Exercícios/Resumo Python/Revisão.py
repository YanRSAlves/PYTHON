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

porta = 'a'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarme disparado? ' + str(alarme)

print(msg)
