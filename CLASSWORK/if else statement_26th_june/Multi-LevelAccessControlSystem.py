'''
---------------------- Access Level Management System ----------------------

Assign access levels based on:

Roles:
Admin
Manager
Employee
Guest

Conditions:
Admin + Security Clearance >= 5 -> Full Access
Manager + Experience > 5 Years -> Department Access
Employee + Experience > 2 Years -> Limited Access
Guest -> Read-Only Access
Inactive Account -> No Access

Sample Input

Role : Admin
Security Clearance : 6
Account Status : Active

------------------------------------------

Sample Output

Access Level : FULL ACCESS

-------------------------------------------------------------
'''

#--------------------- Coding -----------------------------

# input details
role = input("Role : ").lower()
status = input("Account Status (Active/Inactive) : ").lower()

security = 0
experience = 0

# checking account status
if(status == "inactive"):
    access = "NO ACCESS"
else:

    if(role == "admin"):
        security = int(input("Security Clearance : "))
        if(security >= 5):
            access = "FULL ACCESS"
        else:
            access = "NO ACCESS"
    elif(role == "manager"):
        experience = int(input("Experience (Years) : "))

        if(experience > 5):
            access = "DEPARTMENT ACCESS"
        else:
            access = "NO ACCESS"

    elif(role == "employee"):
        experience = int(input("Experience (Years) : "))

        if(experience > 2):
            access = "LIMITED ACCESS"
        else:
            access = "NO ACCESS"

    elif(role == "guest"):
        access = "READ-ONLY ACCESS"

    else:
        access = "INVALID ROLE"
#----------------------------------------------------------
# displaying output
print("Access Level :", access)
#----------------------------------------------------------
'''
Output :

Role : Admin
Security Clearance : 6
Account Status : Active

Access Level : FULL ACCESS
'''