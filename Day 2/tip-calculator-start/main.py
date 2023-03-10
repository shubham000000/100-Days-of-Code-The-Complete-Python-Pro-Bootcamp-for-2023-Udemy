#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

tip_in_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

number_of_people_split_the_bill = int(input("How many people to split the bill? "))

splitted_amount = (total_bill + (total_bill * tip_in_percentage / 100)) / number_of_people_split_the_bill

final_amount = round(splitted_amount, 2)

final_amount = "{:.2f}".format(splitted_amount)
print(f"Each person should pay: ${final_amount}")

#FAQ: How to Get 2 Decimal Places?
#https://www.udemy.com/course/100-days-of-code/learn/lecture/17841394#questions/13315048

#Floating Point Arithmatic
#https://docs.python.org/3/tutorial/floatingpoint.html
