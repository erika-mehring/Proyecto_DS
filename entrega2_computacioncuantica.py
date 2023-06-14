import numpy as np
from scipy.linalg import hadamard

def binary_inner_product(a, b):
    if len(a) != len(b):
        raise ValueError("Las cadenas deben tener la misma longitud")
    n = len(a)
    result = 0
    for i in range(n):
        result += int(a[i]) * int(b[i])
    return result

def tensor_product(a, b):
    return np.kron(a, b)

# Obtener las entradas de fila y columna
i = int(input("Ingrese el número de fila (i): "))
j = int(input("Ingrese el número de columna (j): "))

# Convertir i y j a binario
i_binary = bin(i)[2:]
j_binary = bin(j)[2:]

# Calcular el producto interno de las cadenas binarias
inner_product = binary_inner_product(i_binary, j_binary)
print("Producto interno de las cadenas binarias: ", inner_product)

# Calcular el producto tensorial de cinco compuertas de Hadamard
hadamard_matrix = hadamard(2**5)
hadamard_product = tensor_product(hadamard_matrix, hadamard_matrix)
result = hadamard_product[inner_product, inner_product]
print("Elemento i, j del producto de las compuertas de Hadamard: ", result)
