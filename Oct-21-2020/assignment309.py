size = 70
m = (2 * size) - 2
for i in range(65, size):
    for j in range(130, m):
        print(end=" ")
    m = m - 1
    for j in range(65, i + 1):
        print(chr(i), end=' ')
    print(" ")