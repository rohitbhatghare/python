import functools
l=[1,3,6,4,3,5]
print("the sum of list element is :",end="")
print(functools.reduce(lambda a,b:a+b,l))

print("The maximumlement of the list:",end="")
print(functools.reduce(lambda a,b: a if a > b else b,l))