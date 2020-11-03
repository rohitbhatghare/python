sz=5
for x in range(sz,-(sz),-1):
    for y in range(1,abs(x)+1):
        print("",end=" ")
    for z in range(sz,abs(x),-1):
        print("*",end=" ")
    print()