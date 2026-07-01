# Program to enter age of 15 persons and display adults (age >= 18)
# Creating empty list
age = []
print("Enter ages:")
# Input ages
for x in range(15):
    n = int(input())
    age.append(n)

# Display all ages
print("Ages are:")
print(age)

# Display adults
print("Persons whose age is 18 or above:")

for x in age:
    if x >= 18:
        print(x)