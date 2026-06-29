'''-----------Student Result Analyzer ---------------'''

#--------------Coding----------------- 

#input number of students---------------------
n = int(input("Enter number of students: "))

#calculations------------------
marks = []
for i in range(n):
    score = int(input(f"Enter marks of student {i+1}: "))
    marks.append(score)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / n
passed = sum(1 for m in marks if m >= 40)
distinction = sum(1 for m in marks if m >= 75)

#---------------display final result-----------------

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Passed:", passed)
print("Students with Distinction:", distinction)
