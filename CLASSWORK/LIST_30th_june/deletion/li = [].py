li = []
print("Enter The Elements of List: ")
for i in range(20):
    m = int(input())
    li.append(m)

num = int(input("Enter the number you want to remove duplicates of: "))

while li.count(num) > 1:
    li.remove(num)
li.reverse()

print("List: ")
print(li)