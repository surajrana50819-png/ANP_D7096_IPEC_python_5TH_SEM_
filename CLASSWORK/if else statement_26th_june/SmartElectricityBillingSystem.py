'''
---------------------- Electricity Bill Calculator ----------------------

Calculate electricity bill using:

Units        Rate
0-100        ₹5/unit
101-300      ₹7/unit
Above 300    ₹10/unit

Additional Rules:
Commercial consumers pay 20% extra.
Bills above ₹5000 attract 5% surcharge.
Senior citizens receive 10% discount.

Sample Input

Units Consumed : 450
Consumer Type (Residential/Commercial) : Commercial
Senior Citizen (Y/N) : Y

------------------------------------------

Sample Output

Base Bill : ₹4500
Commercial Charge : ₹900
Surcharge : ₹270
Senior Citizen Discount : ₹567
Final Bill Amount : ₹5103

-------------------------------------------------------------
'''

#--------------------- Coding -----------------------------
# input details from user
units = int(input("Units Consumed : "))
consumer_type = input("Consumer Type (Residential/Commercial) : ").lower()
senior = input("Senior Citizen (Y/N) : ").upper()
# validate input
if(units < 0):
    exit("Units cannot be negative")
#----------------------------------------------------------
# calculating base bill
if(units <= 100):
    base_bill = units * 5
elif(units <= 300):
    base_bill = units * 7
else:
    base_bill = units * 10
#----------------------------------------------------------
# commercial charge
commercial_charge = 0
if(consumer_type == "commercial"):
    commercial_charge = base_bill * 0.20

bill = base_bill + commercial_charge
#----------------------------------------------------------
# surcharge
surcharge = 0

if(bill > 5000):
    surcharge = bill * 0.05

bill = bill + surcharge
#----------------------------------------------------------
# senior citizen discount
discount = 0

if(senior == "Y"):
    discount = bill * 0.10

final_bill = bill - discount
#----------------------------------------------------------
# displaying output
print("Base Bill : ", base_bill)
print("Commercial Charge : ", commercial_charge)
print("Surcharge : ", surcharge)
print("Senior Citizen Discount : ", discount)
print("Final Bill Amount : ", final_bill)
#----------------------------------------------------------
'''
Output :

Units Consumed : 450
Consumer Type (Residential/Commercial) : Commercial
Senior Citizen (Y/N) : Y

Base Bill :  4500
Commercial Charge :  900
Surcharge :  270
Senior Citizen Discount :  567
Final Bill Amount :  5103
'''