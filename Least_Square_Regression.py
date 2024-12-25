
n = int(input("How many x values do you want to enter? Ans: "))
x=[]
print("Enter x values one by one:")
for i in range(n):
    value = float(input())
    x.append(value)

y = []
print("Enter y values one by one:")
for i in range(n):
    value = float(input())
    y.append(value)

print("Data input completed.\nThe value table:")
print("x   y\n")
for i in range(n):
    print(f"{x[i]}   {y[i]}")

sumx = sum(x)
sumy = sum(y)
sumxy = sum(x[i] * y[i] for i in range(n))
sumxx = sum(x[i] * x[i] for i in range(n))

print(f"The calculated value of sumx, sumy, sumxy, sumxx is: {sumx}, {sumy}, {sumxy}, and {sumxx}.")

a = (sumx * sumxy - sumy * sumxx) / (sumx * sumx - n * sumxx)
b = (sumy * sumx - n * sumxy) / (sumx * sumx - n * sumxx)

print(f"The calculated value of a and b is: {a} and {b}.")
print(f"The best fit value of the curve is: y = {a:.2f} + {b:.2f}x.\n\n")
