# Author --> Deep Gupta
import random
count = 0
lower = int(input("Enter the Lower Bound:"))
upper = int(input("Enter the Upper Bound:"))

value = random.randint(lower, upper)

print("Your Lower Bound is:", lower)
print("Your Upper Bound is:", upper)


Guess = int(input("Enter Your Guess:"))

count += 1
while Guess != value:
    if Guess < value:
        print("Your Guess is Low than the Value")
        Guess = int(input("Enter Your Guess:"))
        count += 1
    elif Guess > value:
        print("Your Guess is High than the Value")
        Guess = int(input("Enter Your Guess:"))
        count += 1
    else:
        break
count += 1
print("You got correct Random Number in " + str(count) + " attempt.")
print("Congratulations! Your Guess is Correct")