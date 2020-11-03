n=5
wx=n
wy=n

for x in range(1,n+1):
    for y in range(1,n*2+1):
        if(y==wx or y==wy):
            print(x,end="")
        else:
            print(" ",end="")
    wx-=1
    wy+=1
    print()