def restar_matrices(A, B):
    # Similar a sumar_matrices, pero restando
    if not A or not B:
        raise ValueError("Matrices vacías")
    filas = len(A)
    columnas = len(A[0])
    if filas != len(B) or columnas != len(B[0]):
        raise ValueError("Matrices deben tener las mismas dimensiones para restar")
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] - B[i][j])
        resultado.append(fila)
    return resultado