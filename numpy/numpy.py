# ===============================
# 📌 1️⃣ Instalando e Importando NumPy
# pip install numpy
# ===============================

import numpy as np  # Importa a biblioteca NumPy

# ===============================
# 📌 2️⃣ Criando Arrays
# ===============================

# Criando um array 1D (vetor)
arr1D = np.array([1, 2, 3, 4, 5])
print(arr1D)  # Saída: [1 2 3 4 5]

# Criando uma matriz 2D
matriz2D = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz2D)
# Saída:
# [[1 2 3]
#  [4 5 6]]

# Criando uma matriz de zeros e uns
zeros = np.zeros((3, 3))  # Matriz 3x3 de zeros
uns = np.ones((2, 4))     # Matriz 2x4 de uns

# Criando um array de números sequenciais
arr_seq = np.arange(2, 10, 2)  # [2 4 6 8]

# Criando um array de números espaçados
arr_linspace = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1. ]

# ===============================
# 📌 3️⃣ Atributos Importantes
# ===============================

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Dimensões do array → (2, 3)
print(arr.size)   # Número total de elementos → 6
print(arr.dtype)  # Tipo dos elementos → int32
print(arr.ndim)   # Número de dimensões → 2

# ===============================
# 📌 4️⃣ Manipulação de Arrays
# ===============================

# Redimensionando um array
arr_reshape = arr.reshape(3, 2)

# Concatenando arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))  # [1 2 3 4 5 6]

# Dividindo um array
partes = np.split(arr, 2)  # Divide em 2 partes

# Transformando um array 1D em 2D (matriz coluna)
arr_coluna = arr[:, np.newaxis]

# ===============================
# 📌 5️⃣ Operações Matemáticas
# ===============================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Operações básicas
soma = a + b  # [5 7 9]
subtracao = a - b  # [-3 -3 -3]
multiplicacao = a * b  # [4 10 18]
divisao = a / b  # [0.25 0.4 0.5]
potencia = a ** 2  # [1 4 9]

# Estatísticas
soma_total = np.sum(arr)  # Soma total
media = np.mean(arr)  # Média
mediana = np.median(arr)  # Mediana
desvio_padrao = np.std(arr)  # Desvio padrão

# Produto Matricial
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)  # Multiplicação de matrizes

# ===============================
# 📌 6️⃣ Indexação e Fatiamento
# ===============================

# Acessando elementos
print(arr[1, 2])  # Acessa o elemento (linha 1, coluna 2)

# Fatiamento (slicing)
print(arr[:, 1])  # Todas as linhas, coluna 1

# ===============================
# 📌 7️⃣ Gerando Números Aleatórios
# ===============================

np.random.seed(42)  # Garante reprodutibilidade

aleatorios = np.random.rand(3)  # 3 números aleatórios entre 0 e 1
inteiros = np.random.randint(1, 10, (2, 2))  # Matriz 2x2 de inteiros entre 1 e 10
normal = np.random.normal(0, 1, 5)  # 5 números de uma distribuição normal

# ===============================
# 📌 8️⃣ Filtragem de Dados
# ===============================

arr = np.array([10, 20, 30, 40])

# Filtrando elementos maiores que 20
filtro = arr[arr > 20]  # [30 40]