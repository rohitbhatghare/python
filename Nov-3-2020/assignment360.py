n=9
wx=n//2+1


for x in range(1,n+1):
    for y in range(1,n+1):
        if(y==wx or y==n-wx+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    if(x<=n/2):
        wx-=1
    else:
      wx+=1
    print()