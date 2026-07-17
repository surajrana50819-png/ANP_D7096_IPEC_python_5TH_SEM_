import mysql.connector

dataconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ads@email132',
    database='stdmanagement'
)

cursorobj = dataconnection.cursor()

sql_query = "UPDATE student SET standard=%s, age=%s WHERE studentID=%s"

# User Input
studentID = input("Enter Student ID: ")
standard = input("Enter New Standard: ")
age = int(input("Enter New Age: "))

values = (standard, age, studentID)

cursorobj.execute(sql_query, values)

dataconnection.commit()

if cursorobj.rowcount > 0:
    print("Data updated successfully")
else:
    print("Student ID not found")

cursorobj.close()
dataconnection.close()