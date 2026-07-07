#Funtion to display max, min , avg value from the list 
def find_max(numbers):
    return numbers.max()
    
def find_min(numbers):
    return numbers.min()
      
def find_average(numbers):
    return numbers.avg()

#-------------------------
#-main program-

#create empty list
numbers=[]
print("Enter any 10 numbers : ")
for i in range(10):
    #input from user 
    m=int(input())
    #push onto the list
    numbers.append(m)

#Display output 
print("list is : ",numbers )
print("Max number in the list : " ,find_max(numbers))
print("Min number in the list : ",find_min(numbers))
print("Avg of numbers in the list : ",find_average(numbers))