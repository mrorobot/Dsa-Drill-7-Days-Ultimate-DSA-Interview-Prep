"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place."""


def making_zero(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col0 = 1  # Variable to track if the first column needs to be zeroed

    # First pass: mark rows and columns that need to be zeroed
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Second pass: set matrix cells to zero based on markers
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

    # Handle the first row
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0

    # Handle the first column
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix

# Example usage
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(making_zero(matrix))

'''
Explaination:
Initialization:

n and m store the dimensions of the matrix.
col0 tracks if the first column needs to be zeroed.
First Pass:

Iterate through the matrix.
If a cell is zero, mark the first cell of the corresponding row and column.
Second Pass:

Iterate through the matrix again.
Set cells to zero if the corresponding row or column is marked.
Handle First Row:

If the first cell of the matrix is zero, zero out the entire first row.
Handle First Column:

If col0 is zero, zero out the entire first column.'''