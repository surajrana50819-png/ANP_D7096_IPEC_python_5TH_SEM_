# Lab 1: Student Marks Management
# Problem: Create a dictionary for 5 students and perform operations

students = {}
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks

# ---- Display all student names and marks
print("All Students:", students)

# ---- Add a new student
new_name = input("Enter new student name: ")
new_marks = int(input(f"Enter marks of {new_name}: "))
students[new_name] = new_marks
print("After Adding:", students)

# ---- Update marks of existing student
update_name = input("Enter student name to update marks: ")
if update_name in students:
    students[update_name] = int(input("Enter new marks: "))
print("After Updating:", students)

# ---- Delete a student
del_name = input("Enter student name to delete: ")
if del_name in students:
    del students[del_name]
print("After Deleting:", students)

# ---- Display student with highest marks
topper = max(students, key=students.get)
print("Topper:", topper, "with marks", students[topper])
