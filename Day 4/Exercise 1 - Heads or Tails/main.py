#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

random_integer = random.randint(0, 1)

if random_integer == 0:
    print("Tails")
elif random_integer == 1:
    print("Heads") 
