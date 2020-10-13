a=int(input("Enter the first number"))
b=int(input("Enter the second number"))

print("Enter the operator which want to perform")

ch =input("Enter any operator from this :- +,-,*,/")
res=0
if ch=='+':
    res=a+b
    print(a, ch, b, ":", res)

elif ch=='-':
    res=a-b
    print(a, ch, b, ":", res)

elif ch=='*':
    res=a*b
    print(a, ch, b, ":", res)

elif ch=='/':
    res=a%b
    print(a, ch, b, ":", res)
else :
    print("Character Not Valid")


