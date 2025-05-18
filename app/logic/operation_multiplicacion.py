def multiplicar_matrices(A, B):
    # Multiplicación clásica de matrices
    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])
    if columnas_A != filas_B:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B para multiplicar")
    resultado = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado