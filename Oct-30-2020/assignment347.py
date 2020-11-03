sz=5
q=1
for x in range(sz,-(sz+1),-1):
    for y in range(1,abs(x)+1):
        print("",end=" ")
    for z in range(sz,abs(x)-1,-1):
        print(str(q),end=" ")
    if(x>0):
        q+=1
    else:
        q-=1


    print()