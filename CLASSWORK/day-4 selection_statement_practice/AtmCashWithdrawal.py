'''
---------------------- ATM Cash Withdrawal ----------------------

Withdraw money only if withdrawal amount
does not exceed available balance.

Sample Input

5000
4500
------------------------------------------
Sample Output

Transaction Successful
------------------------------------------------------------
'''
#--------------------- Coding -----------------------------

balance = float(input("Enter Account Balance : "))
withdraw = float(input("Enter Withdrawal Amount : "))

if(withdraw <= balance):
    print("Transaction Successful")

else:
    print("Insufficient Balance")