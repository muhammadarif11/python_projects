#Bill cost and tip calculator

#User greeting prompt
print("Hey there! Calculating tips has never been easier!")

#System asks the user for the total cost and tip
Cost = float(input("\nWhat is the cost of the bill ($)? "))
Tip = float(input("\nWhat percentage would you like to split? (TIP: standard is 10,12,15 and 20 percent) "))

#Tip calculations
percentage = float(Tip/100)
final_tip = percentage * Cost
final_cost = (percentage+1) * Cost

#Asking the user on how to split the bill and tip
number_of_people = int(input("\nHow many people would you like to split it with? (Put 1 if you are not splitting.)"))
tip_pp = final_tip / number_of_people
cost_pp = round(final_cost/ number_of_people, 2)
initial_cost = round(float(Cost/ number_of_people),2)

#System returns to the user the final tip with a cost breakdown
print(f"\n\nAt a tip of {Tip} percent, each person pays ${cost_pp}. "
      f"This is ${initial_cost} per person, and an additional ${tip_pp} in tip each.")


