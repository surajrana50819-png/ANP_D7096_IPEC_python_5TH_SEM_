# Program to display numbers at odd positions
# Creating a list
numbers = [40, 90, 23, 87, 91, 45, 68, 34, 84]
# Displaying the list
print("List is:")
print(numbers)

print("--------------------")
print("Elements at odd position:")

for index in range(0, len(numbers), 2):
    print(numbers[index], end=" ")