import random
import string

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
length = int(input("Enter the length of the password: "))
password = ''.join(random.choice(characters) for _ in range(length))

print("Your password is:", password)
print("Thank you for using this program!")

