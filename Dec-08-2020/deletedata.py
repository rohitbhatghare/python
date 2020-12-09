import csv
lines = list()
eid= input("Please enter a member's ID to be deleted.")
#name  = input("Please enter name")
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

print("Your data deleted successfully")