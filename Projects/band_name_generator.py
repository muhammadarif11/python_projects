#Day 2: tip calculator
print("Welcome to the tip calculator!")
cost = int(input("What was the total bill cost? "))
people = int(input('How many people would you like to split with? '))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
print("Each person should pay " + int(cost) * int(tip_percent))

