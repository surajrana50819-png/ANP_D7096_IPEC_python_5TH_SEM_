# Lab 5: Student Subject Report Card
# Problem: Nested dictionary with marks in 3 subjects

report_card = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    math = int(input("Enter Math marks: "))
    sci = int(input("Enter Science marks: "))
    eng = int(input("Enter English marks: "))
    report_card[name] = {'Math': math, 'Science': sci, 'English': eng}

# ---- Calculate total marks of each student
totals = {}
for student, subjects in report_card.items():
    totals[student] = sum(subjects.values())
print("Total Marks:", totals)

# ---- Calculate average marks of each student
averages = {}
for student, subjects in report_card.items():
    averages[student] = sum(subjects.values()) / len(subjects)
print("Average Marks:", averages)

# ---- Display topper
topper = max(totals, key=totals.get)
print("Topper:", topper, "with total", totals[topper])

# ---- Subject-wise highest marks
print("Subject-wise Highest Marks:")
for subject in ['Math', 'Science', 'English']:
    highest_student = max(report_card, key=lambda s: report_card[s][subject])
    print(subject, ":", report_card[highest_student][subject], "by", highest_student)

# ---- Students with average >= 85
print("Students with average >= 85:")
for student, avg in averages.items():
    if avg >= 85:
        print(student, ":", avg)
