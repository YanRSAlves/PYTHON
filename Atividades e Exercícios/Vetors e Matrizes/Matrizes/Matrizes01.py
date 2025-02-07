
'''
def inteiros(matriz):
    tem_positivo = False
    tem_negativo = False

    for linha in matriz:
        for numero in linha:
            if numero > 0:  # Verifica se o número é positivo
                tem_positivo = True
            elif numero < 0:  # Verifica se o número é negativo
                tem_negativo = True
            # Se já encontrou ambos, não precisa continuar
            if tem_positivo and tem_negativo:
                return True
    return False





def contar_pares(matriz):
    quantidade = 0
    for linha in matriz:
        for numero in linha:
            if numero % 2 == 0:  # Verifica se o número é par
                quantidade += 1
    return quantidade

# Exemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(inteiros(matriz))
print(contar_pares(matriz))  # Saída: 4


matriz = [
    [1, 2, 3],
    [-1, -2, 0],
    [5, 6, -7]
]

def maior_e_menor(matriz):

    maior = float('-inf')
    menor = float('inf')

    for linha in matriz:
        for numero in linha:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

    return maior, menor


maior, menor = maior_e_menor(matriz)
print(f"Maior: {maior}, Menor: {menor}")





matriz = [
    ['a', 'b'],
    ['c', 'd']
]
vetor = ['a', 'd']

def busca(matriz, elemento):
    for linha in matriz:
        if elemento in linha:
            return True
    return False

def vetor_em_matriz(matriz, vetor):
    cont = 0
    for elemento in vetor:
        if busca(matriz, elemento):
            cont += 1
    return cont

print(vetor_em_matriz(matriz, vetor))


def coluna_maior_somatorio(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    somas = [0]*colunas

    for i in range(linhas):
        for j in range(colunas):
            somas[j] += matriz[i][j]

    maior = max(somas)
    return somas.index(maior)+1



    def colunas(matriz):
    n_colunas = len(matriz[0])
    somatorios = []

    for j in range(n_colunas):
        somatorio = 0
        for i in range(len(matriz)):
            somatorio += matriz[i][j]
        somatorios.append(somatorio)


    return somatorios.index( max(somatorios) )+1
matriz = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]
print(colunas(matriz))
'''
