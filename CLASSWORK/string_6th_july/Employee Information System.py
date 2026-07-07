# Lab 3: Employee Information System
# Problem: Dictionary with Employee ID as key and details as nested dictionary

employees = {}
n = int(input("Enter number of employees: "))
for i in range(n):
    eid = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    employees[eid] = {'Name': name, 'Department': dept, 'Salary': salary}

# ---- Display all employee details
print("All Employees:", employees)

# ---- Search employee by ID
emp_id = int(input("Enter Employee ID to search: "))
print("Search Result:", employees.get(emp_id, "Not Found"))

# ---- Increase salary of all employees by 10%
for eid in employees:
    employees[eid]['Salary'] *= 1.10
print("After Salary Increment:", employees)

# ---- Display employees of a specific department
dept = input("Enter department to filter: ")
print("Employees in", dept, "Department:")
for eid, details in employees.items():
    if details['Department'] == dept:
        print(details)
