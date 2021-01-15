def multiplication_table(size):
    return [[(row * col) for row in range(1, size+1)] for col in range(1, size+1)]

print(multiplication_table(3))