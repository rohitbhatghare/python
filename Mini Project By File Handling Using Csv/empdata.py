import csv


def create():
    with open("empdata.csv", "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["EID", "ENAME", "EPNO", "EADD"])

        eno = int(input("Enter number of employees : "))
        for i in range(eno):
            eid = input("Enter employee ID")
            ename = input("Enter name")
            epno = input("Enter mobile number")
            eadd = input("Enter address")
            w.writerow([eid, ename, epno, eadd])

    print("Your File Created Successfully")
    menu()


def update():
    with open("empdata.csv", "a", newline="") as f:
        w = csv.writer(f)
        eno = int(input("Enter number of employees : "))
        for i in range(eno):
            eid = input("Enter employee ID")
            ename = input("Enter name")
            epno = input("Enter mobile number")
            eadd = input("Enter address")
            w.writerow([eid, ename, epno, eadd])

    print("Your File Updated Successfully")
    menu()


def delete():
    lines = list()
    eid = input("Please enter a member's ID to be deleted : ")
    with open('empdata.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == eid:
                    lines.remove(row)
    with open('empdata.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    print("Your Data Deleted Successfully")
    menu()


def display():
    with open('empdata.csv', 'rt') as f:
        data = csv.reader(f)
        for row in data:
            print(row)
    print("Your Whole Data")
    menu()


def qu():
    print("Exiting Program!!  Bye !! ")


def menu():
    print("Choose Options To Perform : ")
    print("1.Create")
    print("2.Update")
    print("3.Delete")
    print("4.Display All")
    print("5.Exit")
    print("Enter Your Choice :")
    choice = int(input())
    if choice == 1:
        create()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    elif choice == 4:
        display()
    elif choice == 5:
        qu()
    else:
        print("Invalid Choice")
        menu()


menu()