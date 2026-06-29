'''---Password Strength Checker---'''
#----This program checks the strength of a password based on certain criteria.--
#password length should be at least 8 characters long.
while True:
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password is too short. It must be at least 8 characters long.")
    else:
        print("Password length is sufficient.")
        break
#---------------------------------------------