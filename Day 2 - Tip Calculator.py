print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
ppl = int(input("How many people to split the bill? "))
total_tip = (bill*tip)/100
total = bill + total_tip
amount = total / ppl
print("Each person should pay: ${}".format(round(amount,2)))