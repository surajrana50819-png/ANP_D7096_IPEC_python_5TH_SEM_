#WAP a program to take 15 number from user in tuple and display odd number 

#create empty list
list=[]
list2=[]
print("Enter any 15 numbers: ")
for i in range(15):
    #input from user
    m=int(input())
    #check iff input is odd
    if m%2!=0:
        #add odd numbers into list
        list.append(m)
    #add all numbers into the list
    list2.append(m)
#create tuple or convert into tuple 
My_tuple=tuple(list)
my_tuple2=tuple(list2)
#display tuple 
print(my_tuple2)
#display tuple containing odd numnbers
print(My_tuple)