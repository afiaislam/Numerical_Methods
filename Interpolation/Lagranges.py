
x=[3,5,7,9]
y=[46,66,80,101]
inp_x=4

n=len(x)
result=0
for i in range(n):
    denom=1
    nom=1
    for j in range(n):
        if i!=j:
            denom=denom*(x[i]-x[j])
            nom=nom*(inp_x-x[j])
    result=result+((nom/denom)*y[i])

print("Result= ",result)