'''--------employee salary statistics---------'''


#------------Coding------------
n = int(input("Enter number of employees: "))

salaries = []
for i in range(n):
    salary = int(input(f"Enter salary of employee {i+1}: "))
    salaries.append(salary)

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / n
above_50k = sum(1 for s in salaries if s > 50000)
#display output 
print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees earning more than ₹50,000:", above_50k)
