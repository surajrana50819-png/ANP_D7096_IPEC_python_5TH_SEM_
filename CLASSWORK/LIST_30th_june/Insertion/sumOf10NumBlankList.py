# Program to find out sum of 10 numbers using blank list
# Creating blank list
numbers = []
# Input 10 numbers
for x in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
# Display numbers
print("Numbers are:")
print(numbers)
# Finding sum
sum = 0

for x in numbers:
    sum = sum + x

print("Sum =", sum)