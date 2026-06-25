# Compound Growth of Savings
initial_amount = float(input("Enter initial amount: "))
years = int(input("Enter number of years: "))

final_amount = initial_amount * (2 ** years)

print("Final Amount after", years, "years:", final_amount)
