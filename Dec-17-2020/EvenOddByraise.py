class EVodd(Exception):
    pass


num= int(input("Enter the number"))

if (num %2== 0):
    raise EVodd("Even number")
else:
    raise EVodd("Odd number")
