# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
current_age = int(age)

total_lifespan_year = 90

number_of_days_in_a_year = 365
number_of_weeks_in_a_year = 52
number_of_months_in_a_year = 12

remaining_days = (total_lifespan_year - current_age) * number_of_days_in_a_year
remaining_weeks = (total_lifespan_year - current_age) * number_of_weeks_in_a_year
remaining_months = (total_lifespan_year - current_age) * number_of_months_in_a_year

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")

#Tim Urban's Life in Weeks
#https://waitbutwhy.com/2014/05/life-weeks.html
