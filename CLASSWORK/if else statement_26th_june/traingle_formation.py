'''------- Problem Statement: Check Whether Three Angles Form a Triangle

Write a Python program that accepts three angles (in degrees) from the user 
and check whether they form a valid triangle.
Display an appropriate message based on the result.
-------------------------------------------------------------'''
#------- Coding ---------------
#input of first angle from the user
angle1 = float(input("Enter first angle(in degrees) :"))
#validate the angle
if(angle1 <= 0):
    exit("Angle must be positive")
#--------------------------------------------------------------
#input of second angle from the user
angle2 = float(input("Enter second angle(in degrees) :"))
#validate the angle
if(angle2 <= 0):
    exit("Angle must be positive")
#--------------------------------------------------------------
#input of third angle from the user
angle3 = float(input("Enter third angle(in degrees) :"))
#validate the angle
if(angle3 <= 0):
    exit("Angle must be positive")
#--------------------------------------------------------------
print("--------------------------------------------")
#to verify three angles form a triangle or not
if( angle1 + angle2 + angle3 == 180):
    print("Above angles form a triangle")
else:
    print("Above angles do not form any triangle")

#----------------------------------------------------
'''Output : 
Enter first angle(in degrees) :45
Enter second angle(in degrees) :78
Enter third angle(in degrees) :120
--------------------------------------------
Above angles do not form any triangle
--------------------------------------------'''