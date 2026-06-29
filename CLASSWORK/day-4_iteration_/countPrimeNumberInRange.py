'''------Count Prime Number In a Rnage--------'''

# Accept two integers from the user
start = int(input("Enter the starting value of the range: "))
end = int(input("Enter the ending value of the range: "))

#------Coding--------------
prime_count = 0

print(f"\nPrime numbers between {start} and {end} are:")

for num in range(start, end + 1):
  
    if num < 2:
        continue
   
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
        prime_count += 1

# Finally, display the total count of prime numbers
print(f"\n\nTotal prime numbers found = {prime_count}")
