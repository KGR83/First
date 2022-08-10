import random
import math
# Taking Inputs
lower = 0

# Taking Inputs
upper= 50


x = random.randint(0,50)


if x==26:
    print("Woohoo! You did it! Congrats, you did it!")
elif x > 26:
    print("Sorry, you have guessed too small. Please guess again.")
elif x < 26:
    print("Sorry, you have guessed too big. Better luck next time.")