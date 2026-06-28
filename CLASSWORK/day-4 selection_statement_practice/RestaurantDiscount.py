'''
---------------------- Restaurant Discount ----------------------

Bill below ₹1000 -> No Discount
₹1000-₹2999 -> 10% Discount
₹3000 or more -> 20% Discount

Sample Input
3200
------------------------------------------
Sample Output
20% Discount Applied
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------
bill = float(input("Enter Total Bill Amount : "))

if(bill < 1000):
    print("No Discount")

elif(bill < 3000):
    print("10% Discount Applied")

else:
    print("20% Discount Applied")