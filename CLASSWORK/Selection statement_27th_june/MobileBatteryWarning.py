'''
---------------------- Mobile Battery Warning ----------------------

Display warning only when battery percentage
is below 15%.

Sample Input
10
------------------------------------------
Sample Output
Connect Charger Immediately
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------

battery = int(input("Enter Battery Percentage : "))

if(battery < 15):
    print("Connect Charger Immediately")