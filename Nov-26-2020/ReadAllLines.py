L = ["Nishant\n", "Rohit\n", "Abhilash\n"]

f = open('abc.txt', 'w')
f.writelines(L)
f.close()

f = open('abc.txt', 'r')
l1 = f.readlines()
print(l1)
f.close()