'''
---------------------- Premium Membership Eligibility ----------------------

A customer becomes Premium Member if:

Total Purchases > ₹50,000
Orders Completed >= 20
Customer Rating >= 4.5

Special Case:
Purchases above ₹1,00,000 automatically qualify.

Sample Input

Total Purchases : 120000
Orders Completed : 10
Customer Rating : 4.0

------------------------------------------

Sample Output

Premium Membership Status : Eligible
Reason : Purchase amount exceeded ₹100000.

-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------
# input details from user
total_purchases = float(input("Total Purchases : "))
orders_completed = int(input("Orders Completed : "))
customer_rating = float(input("Customer Rating : "))
# validate input
if(total_purchases < 0 or orders_completed < 0 or customer_rating < 0):
    exit("Invalid Input")
#----------------------------------------------------------
# checking premium membership eligibility
if(total_purchases > 100000):
    status = "Eligible"
    reason = "Purchase amount exceeded ₹100000."
elif(total_purchases > 50000 and orders_completed >= 20 and customer_rating >= 4.5):
    status = "Eligible"
    reason = "All eligibility conditions satisfied."
else:
    status = "Not Eligible"
    reason = "Eligibility conditions not satisfied."
#----------------------------------------------------------
# displaying output
print("Premium Membership Status :", status)
print("Reason :", reason)
#----------------------------------------------------------
'''
Output :

Total Purchases : 120000
Orders Completed : 10
Customer Rating : 4.0

Premium Membership Status : Eligible
Reason : Purchase amount exceeded ₹100000.
'''