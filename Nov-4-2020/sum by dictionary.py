n= int(input("Enter the number of students"))

d={}
for i in range (n):
    print("enter the name of student")
    keys=input()
    print("Enter marks")
    values=int(input())
    d[keys]=values

print(d)
sum1=sum(d[items] for items in d)
print(sum1)