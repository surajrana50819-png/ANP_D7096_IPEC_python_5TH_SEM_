'''-----login system with max attempts------'''


# --------Coding---------------

correct_username = "admin"
correct_password = "python123"

for attempt in range(1, 4):
    print(f"Attempt {attempt}")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == correct_username and password == correct_password:
        print("\nLogin Successful")
        break
    else:
        print("\nInvalid Credentials\n")
else:
    print("Account Locked")
