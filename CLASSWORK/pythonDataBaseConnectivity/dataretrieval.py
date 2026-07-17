#to import mysql.connector module
import mysql.connector
#------------------------------------------------------------
#to establish connection with mysql
dataconnection = mysql.connector.connect(host = 'localhost',
	user = 'root',
	password = 'Ads@email132',
	database = 'stdmanagement'
	)
#------------------------------------------------------------
# to create a cursor object
cursorobj = dataconnection.cursor()
#------------------------------------------------------------
# writing select query
sql_query = 'select * from student'

#------------------------------------------------------------
#to execute the query
cursorobj.execute(sql_query)
#------------------------------------------------------------
#to fetch all data
#data = cursorobj.fetchall() #this stores data in memory hence less efficient
#------------------------------------------------------------
data = False
for row in cursorobj:
	data = True
	print("Student id : ",row[0])
	print("Student Name : ",row[1])
	print("Standard : ",row[2])
	print("Age : ",row[3],"Year")
	print("----------------------------")
#------------------------------------------------------------
if(data == False):
	print("No data found")
#to close cursur object
cursorobj.close()
#to close connection object
dataconnection.close()
#------------------------------------------------------------