def f(x):
    return x**3 - x**2 - 2

def bisection_method(f, a,b ):
    
    if f(a)*f(b)>=0:

        print("bisection method fail.")
        return None
    
    c=a

    while abs(0-f(c))>= 1e-6:

        c=(a+b)/2

        if f(c)==0:
            break
        elif f(c)*f(a)<0:
            b=c
        else:
            a=c
            
    return c

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

z=bisection_method(f, a,b )
print(f"The value of the root is approximately: {z:.4f}")           