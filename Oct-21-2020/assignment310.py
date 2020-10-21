size = 70
m = (2 * size) - 2
ch=65
for i in range(64, size):
    for j in range(130, m):
        print(end=" ")
    m = m - 1
    for j in range(64, i + 1):
        c=chr(ch)

        print(c, end=' ')
    ch+= 2
    print(" ")