import mysql.connector

dataconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ads@email132',
    database='stdmanagement'
    )
#create a cursorobj
cursorobj = dataconnection.cursor()

sql_query = "DELETE FROM student WHERE studentID=%s"

# User Input
studentID = input("Enter Student ID to delete: ")

values = (studentID,)

# Execute Query
cursorobj.execute(sql_query, values)

# Commit Changes
dataconnection.commit()

# Check Data Deleted or Not
if cursorobj.rowcount > 0:
    print("Data deleted successfully")
else:
    print("Student ID not found")

# Close Cursor and Connection
cursorobj.close()
dataconnection.close()
