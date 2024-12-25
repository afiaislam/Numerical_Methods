def f(x):
    return x**3 - 5*x + 3

def df(x):
    return 3*x**2 - 5 

def newtonRaphson(x, f, df):

    while abs(0-f(x))>1e-6:
        
        if abs(df(x)) < 1e-6:  
            print("Derivative too small; no convergence.")
            return None
        
        x_new = x - f(x) / df(x)  
        if abs(x_new - x) < 0.001: 
            return x_new  
        
        x = x_new  
    
    print("Maximum iterations reached; no convergence.")
    return None  

x = float(input("Enter the initial guess: "))
ans = newtonRaphson(x, f, df)

if ans is not None:
    print(f"The value of the root is approximately: {ans:.4f}")
