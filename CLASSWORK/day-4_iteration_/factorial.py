''' Program to display factorial of the given number'''
#input of number from user
num = int(input("Enter any number : "))
#------------------------------------------
if(num == 0 ):
    print("Factorial is 1")
elif(num < 0):
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    for x in range(1,num + 1):
        factorial = factorial * x
#------------------------------------------
#display result
    print("Factorial of", num, "is", factorial)