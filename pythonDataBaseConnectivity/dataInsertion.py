#to import mysql connector 
import mysql.connector
#to establish connection with mysql 
dataconnection = mysql.connector.connect(host =  'localhost',
	user = 'root',
	password = 'Ads@email132',
	database = 'stdmanagement'
	)
#to create a cursor object 
cursorobj = dataconnection.cursor()
#---------------------------------------
sql_query = 'insert into student values (%s,%s,%s,%s)'

studentID = 'std101'
studentName = 'suraj'
standard = '10th'
age = 15
values = (studentID,studentName,standard,age)

#to excute query 
cursorobj.execute(sql_query , values)
#-----------------------------------
#to commit changes
dataconnection.commit()
#-----------------------------------
#to check data inserted or not 
if(cursorobj.rowcount > 0):
	print('Data inserted successfully')
else:
	print('unable to insert data')
#-----------------------------------
#to close cursor object 
cursorobj.close()
#to close dataconnection object 
dataconnection.close()
#-----------------------------------
