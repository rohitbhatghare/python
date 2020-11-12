def fun(n):
    if n==1:
        return n
    else:
        return n * fun(n - 1)

num=int(input("Enter the Number "))
print(fun(num))