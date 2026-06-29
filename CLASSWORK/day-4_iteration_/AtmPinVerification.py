'''--------program to verify the pin of an atm card-------'''
#----Correct pin is 4589------
CORRECT_PIN = 4589
#----input pin from user------
PIN = int(input("Enter your pin : "))
#----check the pin------
while PIN != CORRECT_PIN:
    print("INVALID PIN")
else:
    print("ACCESS GRANTED") 