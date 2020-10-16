str = input("Enter the string")
l = len(str)
p = l-1
index = 0
while index < p:
    if str[index] == str[p]:
        index = index + 1
        p = p-1
        print("String is a palindrome")
        break
    else:
        print("string is not a palindrome")
        break