import numpy as np

# Crear una matriz de ceros de tipo entero 3x4
matriz_ceros = np.zeros((3, 4), dtype=int)
print("Matriz de ceros:")
print(matriz_ceros)

# Crear una matriz de ceros de tipo entero 3x4 excepto la primera fila que será uno
matriz_unos = np.zeros((3, 4), dtype=int)
matriz_unos[0] = 1
print("Matriz con primera fila de unos:")
print(matriz_unos)

# Crear una matriz de ceros de tipo entero 3x4 excepto la última fila que será el rango entre 5 y 8
matriz_rango = np.zeros((3, 4), dtype=int)
matriz_rango[2] = np.arange(5, 9)
print("Matriz con última fila de rango entre 5 y 8:")
print(matriz_rango)


# Crear un vector de 10 elementos, siendo los índices impares unos y los índices pares dos.
vector = np.zeros(10, dtype=int)
vector[1::2] = 1
vector[::2] = 2
print("Vector:")
print(vector)

# Crear un «tablero de ajedrez», con unos en las casillas negras y ceros en las blancas.
tablero = np.zeros((8, 8), dtype=int)
tablero[1::2,::2] = 1
tablero[::2,1::2] = 1
print("Tablero de ajedrez:")
print(tablero)

# Crear una matriz aleatoria 5x5
matriz_aleatoria = np.random.rand(5, 5)
print("Matriz aleatoria:")
print(matriz_aleatoria)

# Encontrar los valores mínimo y máximo de la matriz
minimo = np.min(matriz_aleatoria)
maximo = np.max(matriz_aleatoria)
print("Valor mínimo: ", minimo)
print("Valor máximo: ", maximo)


# Normalizar la matriz
matriz_normalizada = (matriz_aleatoria - minimo) / (maximo - minimo)
print("Matriz normalizada:")
print(matriz_normalizada)
