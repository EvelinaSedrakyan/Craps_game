import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"The sum of dice is {die1} + {die2} = {total}")
    return total

print("Welcome to Craps!\n")

total = roll_dice()

if total == 7 or total == 11:
    print("You won")

elif total == 2 or total == 3 or total == 12:
    print("You lose")

else:
    goal = total
    print(f"Now your goal number is {goal}")

    while True:
        total = roll_dice()

        if total == goal:
            print("You won")
            break
        elif total == 7:
            print("You lose")
            break
