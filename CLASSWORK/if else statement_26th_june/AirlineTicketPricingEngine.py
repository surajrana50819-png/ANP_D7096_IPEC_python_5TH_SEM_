'''---------Airline Ticket Pricing Engine---------
An airline calculates ticket fare using: 
Base Fare = ₹5000 
Additional Charges: 
• Business Class → +₹3000  
• Window Seat → +₹500  
• Weekend Travel → +₹1000  

Discounts: 
• Age below 12 → 50%  
• Age above 60 → 20%  

Calculate the final ticket fare. 

Sample Input 
Enter Passenger Age: 65 
Business Class (Y/N): Y 
Window Seat (Y/N): Y 
Weekend Travel (Y/N): Y 

Sample Output 
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0'''

#--------------------- Coding -----------------------------
# input details from user
passenger_age = int(input("Enter passenger Age:"))
Business_Class = input("Business Class (Y/N):")
Window_Seat = input("Window Seat (Y/N):")
Weekend_Travel = input("Weekend Travel (Y/N):")
#validate input
if(passenger_age <0):
    exit("Age must be positive")
#----------------------------------------------------------
# calculating ticket fare
Base_fare = 5000
additional_charges = 0
if Business_Class.upper() == 'Y':
    additional_charges += 3000
    if Window_Seat.upper() == 'Y':
        additional_charges += 500
    if Weekend_Travel.upper() == 'Y':
        additional_charges += 1000
#----------------------------------------------------------
# calculating discount
discount = 0 
if passenger_age < 12:
    discount = 0.5
elif passenger_age > 60:
    discount = 0.2
#----------------------------------------------------------
# calculating final ticket fare
final_ticket_fare = (Base_fare + additional_charges) * (1 - discount)
#----------------------------------------------------------