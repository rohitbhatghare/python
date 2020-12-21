import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='csv', user='root', password='root')
    cursor = con.cursor()
    eid=int(input("Enter id"))
    sname=input("name")
    eadd=input("address")
    cursor.execute("""INSERT INTO student (ID,Name,Address) VALUES (%s,%s,%s)""",(eid,sname,eadd))
    con.commit()
    print("success")
    cursor.close()
    con.close()
except Exception as ob:

    print("error occured",ob)
