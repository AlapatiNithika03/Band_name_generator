print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
bf = float(bill)
tip = int(tip)
people = int(people)
total = bf * (tip/100+1)
split = round((total/people),2)
print(f"Each person should pay: ${split} ")
