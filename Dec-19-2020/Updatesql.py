import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='csv', user='root', password='root')
    cursor = con.cursor()
    eid = int(input("Enter id"))
    sname = input("Enter the New name")
    eadd = input("Enter the New address")
    cursor.execute("""UPDATE student SET name=%s, address=%s where id=%s """, (sname,eadd,eid))
    con.commit()
    print("record updated")
    cursor.close()
    con.close()
except Exception as ob:

    print("error occured in record",ob)
