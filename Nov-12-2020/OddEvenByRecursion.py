def odev(n):
    if n < 0:
        return n % 2 == 0

    return odev(n - 2)


n = int(input("Enter the number"))
for n in range(1, n):
    if odev(n) == True:
        print("even Range is:-", n)
for n in range(1, n):
    if odev(n) == False:
        print("odd Range is:-", n)
