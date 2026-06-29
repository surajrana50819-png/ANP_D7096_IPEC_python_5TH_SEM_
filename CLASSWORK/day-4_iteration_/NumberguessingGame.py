'''---Number Guessing Game---
Problem Statement 

A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct.'''
#-------coding-----------
#----secret number-------
secret_num = 37
#-------input from user--------
for i in range(100000000):
    Guessed_num = int(input("Enter number: "))
    if  (Guessed_num < 37):
        print("too low")
    elif (Guessed_num > 37):
        print("too high")
    else:
        print ("correct") 

