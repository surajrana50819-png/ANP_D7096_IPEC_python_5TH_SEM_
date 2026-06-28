'''
---------------------- Scholarship Eligibility Checker ----------------------

Scholarship is awarded based on percentage:

95+      -> 100%
90-94    -> 75%
85-89    -> 50%
80-84    -> 25%
Below 80 -> No Scholarship

Conditions:
Family Income must be below ₹8,00,000.
Students with disciplinary actions receive no scholarship.

Sample Input

Percentage : 92
Family Income : 500000
Disciplinary Action (Y/N) : N

------------------------------------------

Sample Output

Scholarship Awarded : 75%

-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------
# input details from user
percentage = float(input("Percentage : "))
family_income = float(input("Family Income : "))
disciplinary_action = input("Disciplinary Action (Y/N) : ").upper()
# validate input
if(percentage < 0 or percentage > 100 or family_income < 0):
    exit("Invalid Input")
#----------------------------------------------------------
# checking scholarship eligibility
if(family_income >= 800000 or disciplinary_action == "Y"):
    scholarship = "No Scholarship"
else:

    if(percentage >= 95):
        scholarship = "100%"

    elif(percentage >= 90):
        scholarship = "75%"

    elif(percentage >= 85):
        scholarship = "50%"

    elif(percentage >= 80):
        scholarship = "25%"

    else:
        scholarship = "No Scholarship"
#----------------------------------------------------------
# displaying output
print("Scholarship Awarded :", scholarship)
#----------------------------------------------------------
'''
Output :

Percentage : 92
Family Income : 500000
Disciplinary Action (Y/N) : N

Scholarship Awarded : 75%
'''