# Program to calculate average mileage of a car

# Input: total distance traveled (km) and fuel consumed (liters)
distance = float(input("Enter total distance traveled (in km): "))
fuel = float(input("Enter total fuel consumed (in liters): "))

# Calculate mileage
if fuel != 0:
    mileage = distance / fuel
    print(f"Average mileage of the car: {mileage:.2f} km/l")
else:
    print("Fuel consumed cannot be zero.")
