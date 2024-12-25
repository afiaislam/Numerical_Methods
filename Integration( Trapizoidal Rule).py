n=int(input("Enter the size of x: "))
x=[]
y=[]
print("Enter the values of x: ")
for i in range(n):
    a=int(input())
    x.append(a)
print("Enter the values of y: ")
for i in range(n):
    b=int(input())
    y.append(b)
start=1
end=5
h=(x[end]-x[start])/(end-start)
m=y[start]+y[end]
k=0
for i in range(start+1,end):
    k=k+y[i]
result=(h/2)*(m+(2*k))

print("Result= ",result)