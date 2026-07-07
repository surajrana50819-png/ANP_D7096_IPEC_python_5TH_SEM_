# Problem Statement 4: Dictionary Search System
# -------------------------------------------------
# Function: search_student(student_dict, roll_no)
# • Accepts dictionary (Key = Roll Number, Value = Student Name)
# • Searches for given roll number
# • Returns student name if found, else "Student Not Found"
# -------------------------------------------------

# User-defined Function
def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"

# -------------------------------------------------
# Main Program
# Creating dictionary of 5 students
students = {
    101: "Aman",
    102: "Vinay",
    103: "Priya",
    104: "Rohit",
    105: "Sneha"
}

# Accept roll number from user
roll_no = int(input("Enter Roll Number to search: "))

# Call function and display result
result = search_student(students, roll_no)
print("Search Result:", result)
