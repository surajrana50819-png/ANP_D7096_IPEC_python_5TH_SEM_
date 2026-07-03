# Program to create a list of marks and names of 15 students
# and display the names of students eligible for admission
# (Marks > 75)

# Creating empty lists
name = []
marks = []

print("Enter name and marks of 15 students:")

# Input names and marks
for x in range(15):
    n = input("Enter Name: ")
    m = int(input("Enter Marks: "))
    name.append(n)
    marks.append(m)

# Display all students
print("Names are:")
print(name)

print("Marks are:")
print(marks)

# Display eligible students
print("Students eligible for admission are:")

for x in range(15):
    if marks[x] > 75:
        print(name[x])