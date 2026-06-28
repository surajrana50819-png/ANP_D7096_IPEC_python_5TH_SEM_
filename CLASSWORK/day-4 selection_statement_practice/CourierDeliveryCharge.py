'''
---------------------- Courier Delivery Charge ----------------------

Weight up to 2 kg -> ₹50
Weight >2 kg and <=5 kg -> ₹100
Weight >5 kg -> ₹180

Sample Input

4
------------------------------------------
Sample Output

Delivery Charge = ₹100
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------
weight = float(input("Enter Package Weight : "))

if(weight <= 2):
    charge = 50

elif(weight <= 5):
    charge = 100

else:
    charge = 180

print("Delivery Charge = ₹", charge)