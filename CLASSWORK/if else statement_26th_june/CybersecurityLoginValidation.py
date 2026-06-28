'''
---------------------- Login Validation System ----------------------

A login system validates:

Username
Password
OTP

Conditions:
All correct -> Login Successful
Incorrect OTP -> Re-enter OTP
Incorrect Password after 3 attempts -> Account Locked
Incorrect Username -> User Not Found

Sample Input

Username : admin
Password : admin123
OTP : 4567

------------------------------------------

Sample Output

Login Successful
Welcome Admin

-------------------------------------------------------------
'''

#--------------------- Coding -----------------------------
# correct login details
correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"
# input username
username = input("Username : ")
#----------------------------------------------------------
# checking username
if(username != correct_username):
    print("User Not Found")
else:

    # password attempts
    attempts = 0

    while(attempts < 3):

        password = input("Password : ")

        if(password == correct_password):

            otp = input("OTP : ")

            if(otp == correct_otp):
                print("Login Successful")
                print("Welcome Admin")

            else:
                print("Re-enter OTP")

            break

        else:
            attempts += 1

            if(attempts == 3):
                print("Account Locked")

            else:
                print("Incorrect Password")
#----------------------------------------------------------
'''
Output :

Username : admin
Password : admin123
OTP : 4567

Login Successful
Welcome Admin
'''