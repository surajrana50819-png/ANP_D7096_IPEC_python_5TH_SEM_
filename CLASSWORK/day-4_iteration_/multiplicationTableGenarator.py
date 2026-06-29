'''----------Multiplication table Generator-----------'''

# Ask the user for a number
num = int(input("Enter Number: "))
# 'for' loop that runs from 1 to 20
for i in range(1, 21):
# Print the result in a neat format
    print(f"{num} x {i} = {num * i}")
