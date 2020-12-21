import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='csv', user='root', password='root')
    cursor = con.cursor()
    eid = int(input("Enter id"))
    # name = input("Enter the New name")
    # eadd = input("Enter the New address")
    cursor.execute("DELETE FROM student WHERE id=%s",(eid,))
    con.commit()
    print("record deleted")
    cursor.close()
    con.close()
except Exception as ob:

    print("error occured in record", ob)
