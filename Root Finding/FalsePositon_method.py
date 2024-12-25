def f(x):
    return x**3 - x*5 + 3 

def falsePositon(a,b,f):

    if f(a)*f(b) >= 0:
        print("Select another values..")
        return None
    
    c=a

    while abs(0-f(c)) >0.001:
        c= (a*f(b)-b*f(a))/(f(b)-f(a))

        if f(c)==0:
            break
        
        if f(a)*f(c) > 0 :
            a=c
        else:
            b=c

    return c

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

ans= falsePositon(a,b,f)

print(f"The value of the root is approximately: {ans:.4f}")