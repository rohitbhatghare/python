n=5
wx=1
wy=n*2-1

for x in range(1,n+1):
    for y in range(1,n*2+1):
        if(y==wx or y==wy):
            print(wx,end="")
        else:
            print(" ",end="")
    wx+=1
    wy-=1
    print()