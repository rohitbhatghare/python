dec=3
for x in range(dec,-(dec+1),-1):
    for y in range(dec,abs(x)-1,-1):
        print(y," ",end="")
    print(" ")