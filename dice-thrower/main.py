import random

def roll_dice():
    return random.randint(1, 6)

while True:
    print(f"The number of the dice is: {roll_dice()}")

    option = input("Throw again? (y/n): ").lower()

    if option != "y":
        print("Game finished.")
        break
