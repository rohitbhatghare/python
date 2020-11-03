sz=4
q=0
for x in range(sz,-(sz+1),-1):
    for y in range(1,abs(x)+1):
        print("",end=" ")
    for z in range(sz,abs(x)-1,-1):
        print(chr(q+65),end=" ")
    if(x>0):
        q+=1
    else:
        q-=1


    print()