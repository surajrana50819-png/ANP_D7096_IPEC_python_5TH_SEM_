'''
---------------------- Digital Vault Access ----------------------

A digital vault can only be opened if the user enters
the correct security code.

Sample Input
7890
------------------------------------------
Sample Output
Access Granted to the Vault.
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------

code = int(input("Enter Security Code : "))

if(code == 7890):
    print("Access Granted to the Vault.")