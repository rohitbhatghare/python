import module1
a=int(input("Enter the 1st value"))
b=int(input("Enter the 2nd value"))
ch=input("Enter the operator from +,-,/,*")

if ch=='+':
    print(module1.sum(a,b))

elif ch=='-':
    print(module1.sub(a,b))

elif ch=='/':
    print(module1.div(a,b))

elif ch=='*':
    print(module1.mul(a,b))

else:
   print("Invalid operator")