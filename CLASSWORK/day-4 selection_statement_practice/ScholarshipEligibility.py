'''
---------------------- Scholarship Eligibility ----------------------

A university provides scholarship to students
who score 90 or above.

Sample Input

92
------------------------------------------
Sample Output

Scholarship Approved
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------

percentage = float(input("Enter Percentage : "))

if(percentage >= 90):
    print("Scholarship Approved")

else:
    print("Scholarship Not Approved")