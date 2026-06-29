'''--------Bank transaction summary ----------------'''

# Banking Transaction Program

total_deposit = 0
total_withdrawal = 0
while True:
    amount = int(input("Enter transaction amount (0 to finish): "))
    
    if amount == 0:
        break
    elif amount > 0:
        total_deposit += amount
    else:
        total_withdrawal += abs(amount)

final_balance = total_deposit - total_withdrawal
#display final output
print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", final_balance)
