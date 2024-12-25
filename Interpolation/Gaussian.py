def gaussian_interpolation(x_values, y_values, x):
    n = len(x_values)
    diff_table = [[0] * n for _ in range(n)]

    for i in range(n):
        diff_table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    mid_index = n // 2 if n % 2 == 1 else (n // 2) - 1
    h = x_values[1] - x_values[0]
    u = (x - x_values[mid_index]) / h

    result = diff_table[mid_index][0]
    term = 1

    for i in range(1, n):
        if i % 2 == 1:
            term *= (u - (i // 2))
        else:
            term *= (u + (i // 2))
        result += (term / factorial(i)) * diff_table[mid_index - (i // 2)][i]

    return result

def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

x_values = [0,4,8,12,16]  
y_values = [14,24,32,35,40]  
x = 9  

value = gaussian_interpolation(x_values, y_values, x)
print(f"Interpolated value at x = {x} is {value}")
