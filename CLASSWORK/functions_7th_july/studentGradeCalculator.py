#Funtion to calculate student grade
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "fail"
#--------------------------------
#-Main Program-
print("Enter marks of 5 student: ")
for i in range(5):
    marks = float(input("Enter marks: "))
    #validate input 
    if marks > 100 and marks< 0:
        print("Invalid input ")
    else:
        print("grades of students are : ",calculate_grade(marks))