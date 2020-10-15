num=int(input("Enter the  Number"))

sum=0

temp=num

while  temp>0 :
    dig=temp%10
    sum= sum + dig**3
    temp=temp//10

if sum== num :
    print("armstrong")

else :
    print("Not armstrong")

