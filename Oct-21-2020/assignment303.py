num = 5
for i in range(1, 6):

    for j in range(i):
        print("     ", end=" ")
    for k in range(5, i-1, -1):
        print(num, " ", end=" ")
    num -= 1
    print(" ")