# Your code here


def matrix_builder(n):
    
    matrix = []

    for i in range(n):

        row = [1] * n
        matrix.append(row)

    return matrix

resultado = matrix_builder(3)

print(resultado)