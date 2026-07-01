# Program to enter 10 numbers and display odd numbers

# Creating blank list
num = []

print("Enter any 10 numbers:")

for x in range(10):
    n = int(input())
    num.append(n)

# Display all numbers
print("Numbers are:")
print(num)

# Display odd numbers
print("Odd numbers are:")

for x in num:
    if x % 2 != 0:
        print(x)