dec=7
for x in range(4,0,-1):
    for y in range(x,5):
        print(" ",end="")
    for z in range(1,dec+1):
        print(chr(z+64),end="")
    dec-=2
    print()