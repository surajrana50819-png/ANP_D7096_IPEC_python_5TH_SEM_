'''
---------------------- Parking Entry Validation ----------------------

1 -> Valid Pass
0 -> No Pass
Sample Input

0
------------------------------------------
Sample Output

Entry Denied
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------
parking_pass = int(input("Enter Parking Pass (1/0) : "))

if(parking_pass == 1):
    print("Entry Allowed")

else:
    print("Entry Denied")