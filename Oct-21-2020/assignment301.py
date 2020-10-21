
for i in range(65,70):
    for j in range(i, 70, 1):
        print(" ", end=" ")
    for j in range(64, i, 1):
        print(chr(i), end=" ")
    print(" ")