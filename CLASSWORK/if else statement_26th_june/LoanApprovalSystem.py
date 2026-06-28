'''------------ Loan Approval System ------------
A bank evaluates loan applications using: 
• Credit Score ≥ 750  
• Annual Income ≥ ₹8,00,000  
• Existing Loan Amount ≤ ₹2,00,000  

Conditions: 
• All conditions satisfied → Approved  
• Only one condition fails → Manual Review  
• More than one condition fails → Rejected  

Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 

Sample Output 
Loan Status: Manual Review 
Reason: Income criteria not satisfied. '''

#--------------------- Coding -----------------------------
# input details from user
credit_score = int(input("Enter Credit Score: "))
annual_income = float(input("Enter Annual Income: "))   
existing_loan_amount = float(input("Enter Existing Loan Amount: "))
# validate input
if(credit_score < 0 or annual_income < 0 or existing_loan_amount < 0):
    exit("Credit Score, Annual Income and Existing Loan Amount must be positive")
#----------------------------------------------------------
# evaluating loan application
if credit_score >= 750 and annual_income >= 800000 and existing_loan_amount <= 200000:
    print("Loan Status: Approved")
elif (credit_score < 750 and annual_income >= 800000 and existing_loan_amount <= 200000) or \
     (credit_score >= 750 and annual_income < 800000 and existing_loan_amount <= 200000) or \
     (credit_score >= 750 and annual_income >= 800000 and existing_loan_amount > 200000):
    print("Loan Status: Manual Review")
else:
    print("Loan Status: Rejected")
#----------------------------------------------------------
# displaying output
'''Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 

Sample Output
Loan Status: Manual Review
Reason: Income criteria not satisfied. '''