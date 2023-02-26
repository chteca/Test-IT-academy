def transpose_matrix(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("Транспонированная матрица:", transposed_matrix)
    print("Размер исходной матрицы:", len(matrix), "x", len(matrix[0]))
    print("Размер транспонированной матрицы:", len(transposed_matrix), "x", len(transposed_matrix[0]))