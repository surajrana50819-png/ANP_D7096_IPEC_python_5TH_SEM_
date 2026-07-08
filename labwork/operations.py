import twofigures
#MENU FOR USER TO INTERACT
print("===== MENU =====")
print("1. Square")
print("2. Circle")
print("3. Triangle")
print("4. Rectangle")
#INPUT FROM USER
choice = int(input("Enter your choice (1-4): "))
#-----------SQUARE--------
if choice == 1:
    side=int(input("Enter length of sides:"))
    print("1. area ")
    print("2. parameter")
    dimension=int(input("Enter the number: "))
    if dimension==1:
        print("area of square is ",twofigures.square_area(side))
    else:
        print("parameter of square is",twofigures.square_perimeter(side))
#--------CIRCLE----------
elif choice == 2:
    radius=int(input("enter length of radius: "))
    print("1. area ")
    print("2. parameter")
    dimension=int(input("Enter the number: "))
    if dimension==1:
        print("area of circle is ",twofigures.circle_area(radius))
    else:
        print("circumference of circle",twofigures.circle_circumference(radius))
#------------TRIANGLE----------
elif choice == 3:
    base=int(input("Enter base : "))
    height=int(input("ENter height: "))
    print("1. area ")
    print("2. parameter")
    dimension=int(input("Enter the number: "))
    if dimension==1:
        print("area of triangle is ",twofigures.triangle_area(base,height))
    else:
        print("parameter of triangle",twofigures.triangle_perimeter(base,height))

#-----------RECTANGLE------------    
elif choice == 4:
    length=int(input("Enter length : "))
    breath=int(input("ENter breath: "))
    print("1. area ")
    print("2. parameter")
    dimension=int(input("Enter the number: "))
    if dimension==1:
        print("area of rectangle is ",twofigures.rectangle_area(length,breath))
    else:
        print("parameter of rectangle",twofigures.rectangle_perimeter(length,breath))
else:
    print("Invalid Choice!")