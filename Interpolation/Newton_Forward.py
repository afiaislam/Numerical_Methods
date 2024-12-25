def newton_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    M = []                   
    for i in range(n):       
        row = [0] * n       
        M.append(row)       

    for i in range(n):
        M[i][0] = y_values[i]

    for i in range(1, n):
        for j in range(n - i):
            M[j][i] = M[j + 1][i - 1] - M[j][i - 1]
    
    h = x_values[1] - x_values[0]
    u = (x - x_values[0]) / h
    result = M[0][0]

    for i in range(1, n):     
        factor = u
        for j in range(1, i):
            factor *= (u - j)
        result += (factor / factorial(i)) * M[0][i]
    return result

def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

x_values = [3,5,7,9] 
y_values = [46,66,80,101] 
x = 4                     

value = newton_forward_interpolation(x_values, y_values, x)
print("Interpolated value at x =", x, "is", value)