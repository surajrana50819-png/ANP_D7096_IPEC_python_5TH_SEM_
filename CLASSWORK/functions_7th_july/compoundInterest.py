#Funtion to calculate compound interest
def calculate_compound_interest(principal,rate,time):
    return principal*(1*rate/100)**time
#-----------------------------------------
#-main program-
principal=float(input("Enter principal(in Rs):"))
rate=float(input("Enter rate(in %):"))
time=int(input("Enter time(in year):"))
print("Compound interest is : ", calculate_compound_interest(principal,rate,time))