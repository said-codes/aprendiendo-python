import random

# Lists of elements for the story
characters = ["a brave knight", "a clever thief", "a young wizard", "a curious princess"]
places = ["in an ancient castle", "in an enchanted forest", "in a forgotten city", "in an underwater kingdom"]
items = ["a magical sword", "an ancient book", "a lost jewel", "a secret map"]
actions = ["faced a dragon", "discovered a mystery", "rescued a friend", "solved a riddle"]
twists = [
    "but suddenly, an unexpected enemy appeared",
    "and just when everything seemed solved, something went wrong",
    "but discovered they were not alone on their adventure",
    "and it all turned out to be a dream"
]

# Function to generate the story
def generate_story(character, place, item, action, twist):
    return f"Once upon a time, {character} traveled {place} with {item} and {action}, {twist}."

# Initial random selection
character = random.choice(characters)
place = random.choice(places)
item = random.choice(items)
action = random.choice(actions)
twist = random.choice(twists)

while True:
    # Print the story and its elements
    print("\n=== Generated Story ===")
    print(generate_story(character, place, item, action, twist))

    print("\n=== Story Elements ===")
    print(f"Character: {character}")
    print(f"Place: {place}")
    print(f"Item: {item}")
    print(f"Action: {action}")
    print(f"Twist: {twist}")

    # Ask the user if they want to change the story
    answer = input("\nDo you want to change any element of the story? (yes/no): ").lower()
    if answer != "yes":
        print("\nStory finalized!")
        break

    # Ask which element(s) to change
    elements = input("Which element do you want to change? (character/place/item/action/twist/all): ").lower()

    if elements in ["character", "all"]:
        character = input(f"Choose a character from the list {characters}: ")
        if character not in characters:
            print("Invalid choice, selecting a random one.")
            character = random.choice(characters)

    if elements in ["place", "all"]:
        place = input(f"Choose a place from the list {places}: ")
        if place not in places:
            print("Invalid choice, selecting a random one.")
            place = random.choice(places)

    if elements in ["item", "all"]:
        item = input(f"Choose an item from the list {items}: ")
        if item not in items:
            print("Invalid choice, selecting a random one.")
            item = random.choice(items)

    if elements in ["action", "all"]:
        action = input(f"Choose an action from the list {actions}: ")
        if action not in actions:
            print("Invalid choice, selecting a random one.")
            action = random.choice(actions)

    if elements in ["twist", "all"]:
        twist = input(f"Choose a twist from the list {twists}: ")
        if twist not in twists:
            print("Invalid choice, selecting a random one.")
            twist = random.choice(twists)
