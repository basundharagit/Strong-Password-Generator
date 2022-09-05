import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

characters = letters + numbers + symbols
password_chars = []


# taking user input
user_input = int(input("Enter the number of characters you want in your password: "))
for i in range(user_input):
    random_char = random.choice(characters)
    password_chars.append(random_char)


# shuffling randomly the list elements
random.shuffle(password_chars)

# join each character of list
user_password = "".join(password_chars)

print(f"Your password could be: {user_password}")
