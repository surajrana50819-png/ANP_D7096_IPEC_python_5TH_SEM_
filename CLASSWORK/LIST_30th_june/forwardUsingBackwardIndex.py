# Program to display elements of list
# in forward direction using backward index

list1 = [40, 30, 70, 60, 90, 10]

print("List is:")
print(list1)

print("Elements in forward direction using backward index:")

for index in range(-len(list1), 0):
    print(list1[index])