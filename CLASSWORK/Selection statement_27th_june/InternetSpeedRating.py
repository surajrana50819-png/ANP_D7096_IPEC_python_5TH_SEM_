'''
---------------------- Internet Speed Rating ----------------------

Less than 25 Mbps -> Slow
25-99 Mbps -> Good
100 Mbps or above -> Excellent

Sample Input

120

------------------------------------------
Sample Output

Excellent Connection
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------
speed = float(input("Enter Internet Speed (Mbps) : "))

if(speed < 25):
    print("Slow Connection")

elif(speed < 100):
    print("Good Connection")

else:
    print("Excellent Connection")