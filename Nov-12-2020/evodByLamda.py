n=int(input("Enter the number"))
print("Even")
for n in range(n):
    x= lambda n: n if (n%2==0) else ""
    print(x(n))
print("odd")
for n in range(n):
    x= lambda n: n if (n%2==1) else ""
    print(x(n))