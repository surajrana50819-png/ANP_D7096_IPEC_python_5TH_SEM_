#Funtion to calculate simple interest 
def Calulate_simple_interest(principal,rate,time):
    return (principal*rate*time)/100
#------------------------------------------------
#-Main Program-
principal=float(input("Enter principal(in Rs):"))
rate=float(input("Enter rate(in %):"))
time=int(input("Enter time(in year):"))
print("Simple interest : Rs", Calulate_simple_interest(principal,rate,time))