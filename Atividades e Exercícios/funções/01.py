safra = 1978 #variável global

def loja():
    produto= 'vinho tinto'
    global safra #chamada da variável global
    print(produto)
    print(safra)

def soma_de_numeros(valor1, valor2):
    soma = valor1 + valor2
    return soma
def soma(valor1, valor2): return valor1 + valor2
def divisao(valor1, valor2): return valor1 / valor2
def multiplicacao(valor1, valor2): return valor1 * valor2

def numeros(num):
    print('Definindo valores...', num)

# chamada da função loja()
loja()
print(safra)

# chamada da função numeros()
numeros(1_2_3)

# chamada das funções soma() divisão() multiplicacao()
print(soma(1,5))
print(divisao(8,2))
print(multiplicacao(8,2))

# chamada da função soma_dois_numeros()
valor_soma = soma_de_numeros(15,25)

print(valor_soma)
print(soma_de_numeros(50,10))