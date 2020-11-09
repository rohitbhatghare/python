def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

print("Options - \n"\
            "1.add \n"\
            "2.substract \n" \
            "3.Multiplication \n" \
            "4.Division \n")

a=int(input("Select the options from 1,2,3,4   :-  "))

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

if a == 1:
    print(num1 ,"+" ,num2  ,"=",
                 add(num1,num2))
elif a == 2:
    print(num1, "-", num2,"=",
              substract(num1, num2))
elif a == 3:
    print(num1, "*", num2,"=",
          multi(num1, num2))

elif a == 4:
    print(num1, "/", num2,"=",
              divide(num1, num2))
else :
    print("Invaild Option")

