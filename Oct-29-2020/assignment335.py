size=3
for i in range(size,-(size+1),-1):
    for y in range(abs(i),0,-1):
        print(" ",end="")
    for z in range(size,abs(i)-1,-1):
        print(chr(z+65),end="")
    print()