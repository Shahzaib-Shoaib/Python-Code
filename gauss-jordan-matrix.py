def gauss_jordan(matrix):
    # Perform Gauss-Jordan elimination
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        # Make the diagonal element in row i equal to 1
        divisor = matrix[i][i]  # Pivot element
        for j in range(cols):
            matrix[i][j] = matrix[i][j] / divisor  # Pivot row / Pivot element

        # Make other elements in the column i equal to 0
        for k in range(rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(cols):
                    matrix[k][j] = matrix[k][j] - factor * matrix[i][j]

    return matrix


# Example usage:
augmented_matrix = [[5, 0, 7, 40],
                    [0, -5, 2, -5],
                    [0, 0, 12, 60]]

solution = gauss_jordan(augmented_matrix)

print("Solution:")
for row in solution:
    print(row[-1])
