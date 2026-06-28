'''
---------------------- Student Result Calculator ----------------------

A student appears in 5 subjects.

Rules:
Minimum 40 marks in every subject to pass.
Distinction -> Average >= 75
First Division -> Average >= 60
Second Division -> Average >= 50
Pass -> Average >= 40
Fail if any subject score < 40

Sample Input

Hindi : 85
English : 78
Mathematics : 82
Science : 75
Computer : 90

------------------------------------------

Sample Output

Average Marks : 82.0
Result : PASS
Classification : Distinction

-------------------------------------------------------------
'''

#--------------------- Coding -----------------------------
# input marks
hindi = int(input("Hindi : "))
english = int(input("English : "))
maths = int(input("Mathematics : "))
science = int(input("Science : "))
computer = int(input("Computer : "))
# validate input
if(hindi < 0 or hindi > 100 or english < 0 or english > 100 or maths < 0 or maths > 100 or science < 0 or science > 100 or computer < 0 or computer > 100):
    exit("Invalid Marks")

#----------------------------------------------------------
# calculating average
average = (hindi + english + maths + science + computer) / 5
# checking result
if(hindi < 40 or english < 40 or maths < 40 or science < 40 or computer < 40):
    result = "FAIL"
    classification = "Fail"
else:
    result = "PASS"

    if(average >= 75):
        classification = "Distinction"

    elif(average >= 60):
        classification = "First Division"

    elif(average >= 50):
        classification = "Second Division"

    else:
        classification = "Pass"
#----------------------------------------------------------
# displaying output
print("Average Marks :", average)
print("Result :", result)
print("Classification :", classification)
#----------------------------------------------------------
'''
Output :

Hindi : 85
English : 78
Mathematics : 82
Science : 75
Computer : 90

Average Marks : 82.0
Result : PASS
Classification : Distinction
'''