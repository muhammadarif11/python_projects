# Defining main input
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Using age to determine days, weeks, and months left - max age is 90 based on https://waitbutwhy.com/2014/05/life-weeks.html
max_age = 90

days = ((max_age-int(age))*365)
weeks = ((max_age-int(age))*52)
months = int(days/30.4
)

print(f"You have {days} days, {weeks} weeks, and {months} months left")


