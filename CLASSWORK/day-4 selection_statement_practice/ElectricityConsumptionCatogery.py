'''
---------------------- Electricity Consumption Category ----------------------
Up to 100 units -> Low Consumption
101-300 units -> Moderate Consumption
Above 300 units -> High Consumption

Sample Input

245
------------------------------------------
Sample Output

Moderate Consumption
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------
units = int(input("Enter Electricity Units : "))

if(units <= 100):
    print("Low Consumption")

elif(units <= 300):
    print("Moderate Consumption")

else:
    print("High Consumption")