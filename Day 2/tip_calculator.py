print("Welcome to the tip calculator!")
bill = float(input("What was your total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = (tip*bill)/100
total_bill = bill + total_tip
contri = total_bill/people
# print("Each person should pay: $%.2f"% round(contri,2))
print("Each person should pay: ${:.2f}".format(round(contri,2)))