#WAP to remove duplicate of a number 
#create empty list 
list = []
print("Enter any 20 numbers : ")
for i in range(20):
    #input from user
    m=int(input())
    #add to the list
    list.append(m)
print(list)
#enter any number 
print("Enter number whose duplicate is to be deleted: ")
#input dup num from user
duplicate_num=int(input())
#check if the  dup number is present or not 
x = list.count(duplicate_num)
for i in list:
    if x > 1:
        list.reverse()
        list.remove(duplicate_num)
        list.reverse()
    else:
        print("No duplicate found: ")
print("list is : ")
print(list)
        