L = ["Nishant\n", "Rohit\n", "Abhilash\n"]

f = open('abc.txt', 'w')
f.writelines(L)
print(L)
f.close()

f = open('abc.txt', 'r')
l1 = f.readline()
print(l1)
f.close()