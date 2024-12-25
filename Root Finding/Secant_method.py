def f(x):
    return x**3 - 5*x + 3

def secant(f, x0, x1):
    
    while abs(x1 - x0) > 1e-6:
        
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        
        x0 = x1
        x1 = x2
        
    return x1

x0=float(input("Enter the value of x0: "))
x1=float(input("Enter the value of x1: "))

root = secant(f, x0, x1)
print(f"Root is: {root}")
