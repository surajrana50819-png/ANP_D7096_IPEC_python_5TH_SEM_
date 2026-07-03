#create an empty list
my_list=[]
for i in range(10):
    #list input from user
    m=int(input())
    #add element in list
    my_list.append(m)
print("--------------------------")
print ("list before deletion:" , my_list)
print("Input Index to be deleted : ")
#input index from the user
index=int(input())
if index > len(my_list):
    print("invalid index")
#pop element from the list
my_list.pop(index)
#displaying the list after deletion
print("List after deletion : " , my_list)