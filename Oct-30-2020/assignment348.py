sz=5

for x in range(sz,-(sz+1),-1):
    for y in range(1,abs(x)+1):
        print("",end=" ")
    q=1
    for z in range(sz,abs(x)-1,-1):
        print(str(q)+"",end=" ")
        q+=1


    print()