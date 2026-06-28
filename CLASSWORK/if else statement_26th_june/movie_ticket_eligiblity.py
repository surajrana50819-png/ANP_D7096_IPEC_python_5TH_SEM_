'''----------  Movie Ticket Eligibility ------------------
A multiplex allows entry to a movie only if the customer is 18 years of age or older.
Write a Python program that accepts the age of a customer and determines whether they are eligible
to watch the movie.
----------------------------------
Sample Input
Enter Your Age: 21
------------------------------------
Sample Output
You are eligible to watch the movie.
-------------------------------------
Sample Input
Enter Your Age: 15
---------------------------------------
Sample Output
You are not eligible to watch the movie.
--------------------------------------------------------------'''
#--------------------------------------------------------------------------
#--------- Coding ---------------------------------------------------
#input of age from user
age = int(input("Enter age(in year) : "))
#to validate age of the customer
if(age <= 0):
    exit("Age must be positive")
#---------------------------------------------------
#verifying eligibility of the customer
if(age >= 18 ):
    print("You are eligible to watch the movie")
else:
    print("You are not eligible to watch the movie")
#----------------------------------------------------

''' Output : 
Enter age(in year) : 23
You are eligible to watch the movie.
'''