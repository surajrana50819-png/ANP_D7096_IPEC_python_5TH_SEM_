'''
---------------------- Exam Hall Entry ----------------------

1 -> Admit Card Available
0 -> Admit Card Not Available

Sample Input

1

------------------------------------------
Sample Output

Enter Examination Hall
-------------------------------------------------------------
'''
#--------------------- Coding -----------------------------
admit_card = int(input("Enter Admit Card Status (1/0) : "))

if(admit_card == 1):
    print("Enter Examination Hall")