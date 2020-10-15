a=int(input("Enter the three digit number"))

num=a
a1=int(num%10)
num=int(num/10)
a2=int(num%10)
num=int(num/10)
a3=int(num%10)
num=int(num/10)

rev=a1*100+a2*10+a3

print (rev)
