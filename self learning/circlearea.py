"Write a program to calculate area of circle and validate it"
import math
def calculate_area_of_circle(radius):
    # Validate radius
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    
    # Area formula: πr²
    area = math.pi * (radius ** 2)
    return area

# Main program
try:
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area_of_circle(radius)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")
except ValueError as e:
    print(f"Invalid input: {e}")
