s = 4
for x in range(s, -(s + 1), -1):
    for y in range(1, abs(x) + 1):
        print(" ", end="")
    p = 1
    for z in range(s, abs(x) - 1, -1):
        print(chr(p + 64) + " ", end="")
        p += 1
    print()