n=4

for x in range(0,n):
    for y in range(n-1,x,-1):
        print(" ",end="")
    for z in range(0,n):
            print("*",end="")
    print()