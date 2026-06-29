'''------electricity bill analysis----------'''

#-------Coding-------
n = int(input("Enter number of houses: "))
units = []

for i in range(n):
    u = int(input(f"Enter units for house {i+1}: "))
    units.append(u)
# display output 
print("Total units:", sum(units))
print("Average units:", sum(units)/n)
print("Highest consumption:", max(units))
print("Lowest consumption:", min(units))
