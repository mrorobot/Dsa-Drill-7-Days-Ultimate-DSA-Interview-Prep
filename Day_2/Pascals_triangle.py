def printPascal(n:int):
    triangle = []

    for i in range(n):
        # Start with a row of 1s
        row = [1] * (i + 1)
        for j in range(1, i):
            # Compute the value based on the sum of two values from the previous row
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle
print(printPascal(5))