def check_password(password):
    # Check minimum length
    if len(password) < 8:
        return "Weak Password"
    upper = False
    lower = False
    digit = False
    # Check each character
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
    # Check all conditions
    if upper and lower and digit:
        return "Strong Password"
    else:
        return "Weak Password"
# Main Program
password = input("Enter Password: ")
print(check_password(password))