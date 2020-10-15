num=int(input("Enter the  Number"))

sum=0

temp=num

while  temp>0 :
    dig=temp%10
    sum= sum * 10 + dig
    temp=temp//10
print(sum)

if sum== num :
    print("palindrome")

else :
    print("Not palindrome")

