class insufficentbal(Exception):
    pass


wid = int(input("Enter the withdraw money"))
bal = int(input("Enter the balence amount"))
if wid < bal:
    print("please collect your money")
else:
    raise insufficentbal("no money")
