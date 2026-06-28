'''
---------------------- Smart Income Tax Calculator ----------------------

A government tax portal calculates tax based on the following conditions:

Income up to ₹5,00,000      -> No tax
₹5,00,001 to ₹10,00,000     -> 10%
₹10,00,001 to ₹20,00,000    -> 20%
Above ₹20,00,000            -> 30%

Additional Benefits:
Senior Citizen (Age >= 60)  -> 5% rebate on tax
Women Taxpayer (F)          -> 2% rebate on tax

Sample Input
Enter Annual Income : 1200000
Enter Age : 65
Enter Gender (M/F) : F

------------------------------------------

Sample Output

Tax before rebate : ₹240000.0
Senior Citizen Rebate : ₹12000.0
Women Rebate : ₹4800.0
Final Tax Payable : ₹223200.0

-------------------------------------------------------------
'''

#--------------------- Coding -----------------------------

# input details from user
income = float(input("Enter Annual Income : "))
age = int(input("Enter Age : "))
gender = input("Enter Gender (M/F) : ").upper()

# validate input
if(income < 0 or age <= 0):
    exit("Income and Age must be positive")

#----------------------------------------------------------

# calculating tax before rebate
if(income <= 500000):
    tax = 0

elif(income <= 1000000):
    tax = income * 0.10

elif(income <= 2000000):
    tax = income * 0.20

else:
    tax = income * 0.30

#----------------------------------------------------------

# calculating rebates
senior_rebate = 0
women_rebate = 0

if(age >= 60):
    senior_rebate = tax * 0.05

if(gender == "F"):
    women_rebate = tax * 0.02

# final tax calculation
final_tax = tax - senior_rebate - women_rebate

#----------------------------------------------------------

# displaying output
print("Tax before rebate : ₹", tax)
print("Senior Citizen Rebate : ₹", senior_rebate)
print("Women Rebate : ₹", women_rebate)
print("Final Tax Payable : ₹", final_tax)

#----------------------------------------------------------

'''
Output :

Enter Annual Income : 1200000
Enter Age : 65
Enter Gender (M/F) : F

Tax before rebate : ₹ 240000.0
Senior Citizen Rebate : ₹ 12000.0
Women Rebate : ₹ 4800.0
Final Tax Payable : ₹ 223200.0
'''