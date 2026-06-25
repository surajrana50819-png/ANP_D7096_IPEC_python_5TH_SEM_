# Input values
total_students = int(input("Enter total students: "))
students_per_row = int(input("Enter students per row: "))

# Calculate complete rows
complete_rows = total_students // students_per_row

# Output result
print("Number of complete rows:", complete_rows)
