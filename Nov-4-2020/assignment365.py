n=5
wx=n
py=n

for x in range(1,n+1):
    for y in range(1,n*2):
        if(y>wx and y<py):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    wx-=1
    py+=1

    print()