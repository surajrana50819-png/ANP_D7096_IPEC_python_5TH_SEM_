'''
---------------------- Employee Performance Evaluation ----------------------

An employee is evaluated using:

Project Score
Attendance Percentage
Client Feedback Score

Rules:
Excellent -> All scores above 90
Good -> Scores above 75
Average -> Scores above 60
Poor -> Otherwise

Additional Rule:
Attendance below 70% cannot receive more than Average rating.

Sample Input

Project Score : 95
Attendance : 65
Client Feedback : 92

------------------------------------------

Sample Output

Performance Rating : Average
Reason : Attendance below 70%

-------------------------------------------------------------
'''

#--------------------- Coding -----------------------------
# input details from user
project_score = int(input("Project Score : "))
attendance = int(input("Attendance : "))
client_feedback = int(input("Client Feedback : "))

# validate input
if(project_score < 0 or project_score > 100 or
   attendance < 0 or attendance > 100 or
   client_feedback < 0 or client_feedback > 100):
    exit("Scores must be between 0 and 100")
#----------------------------------------------------------
# evaluating performance
if(project_score > 90 and attendance > 90 and client_feedback > 90):
    rating = "Excellent"
elif(project_score > 75 and attendance > 75 and client_feedback > 75):
    rating = "Good"
elif(project_score > 60 and attendance > 60 and client_feedback > 60):
    rating = "Average"
else:
    rating = "Poor"
#----------------------------------------------------------
# checking attendance condition
if(attendance < 70):

    if(rating == "Excellent" or rating == "Good"):
        rating = "Average"

    reason = "Attendance below 70%"
else:
    reason = "Performance based on scores"
#----------------------------------------------------------
# displaying output
print("Performance Rating :", rating)
print("Reason :", reason)
#----------------------------------------------------------
'''
Output :

Project Score : 95
Attendance : 65
Client Feedback : 92

Performance Rating : Average
Reason : Attendance below 70%
'''