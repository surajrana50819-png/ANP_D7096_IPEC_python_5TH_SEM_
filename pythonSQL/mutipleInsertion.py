import mysql.connector 
 
connection = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="Ads@email132", 
    database="stdmanagement" 
) 
 
cursorobj = connection.cursor()
 # SQL Query
sql_query = "INSERT INTO student VALUES (%s,%s,%s,%s)"

# Multiple Records
values = [
    ('std107', 'saksham', '10th',15),
    ('std108', 'sonam', '11th',16),
    ('std109', 'kamal' , '7th',13),
    ('std110', 'reddy', '10th',15)
    ]

# Execute Multiple Insert
cursorobj.executemany(sql_query, values)

# Commit Changes
connection.commit()

# Check Success
if cursorobj.rowcount > 0:
    print(cursorobj.rowcount, "records inserted successfully")
else:
    print("Unable to insert data")

# Close
cursorobj.close()
connection.close()