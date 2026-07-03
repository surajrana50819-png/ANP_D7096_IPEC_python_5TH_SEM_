# Program to find sum of 10 numbers
# Creating a list
numbers = [40, 90, 30, 80, 50, 90, 20, 70, 60, 110]
# Displaying numbers
print("Numbers are:")
print(*numbers)
# Finding sum
sum = 0

for x in numbers:
    sum = sum + x

print("Sum =", sum)