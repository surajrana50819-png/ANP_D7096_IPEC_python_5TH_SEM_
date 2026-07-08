import math
#SQUARE
def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side
#RECTANGLE
def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)
#CIRCLE
def circle_area(radius):
    return math.pi*radius**2
def circle_circumference(radius):
    return 2*math.pi*radius
#TRIANGLE
def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3