dec=1
for x in range (5,0,-1):
    for y in range(x,0,-1):
        print(" ",end="")
    for z in range(1,dec+1):
        print(chr(z+64),end="")
    dec += 2
    print(" ")