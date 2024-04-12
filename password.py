import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    pass_string = ""
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    for i in range(min_length):
        random_index = random.randint(0, len(characters) - 1)
        pass_string += characters[random_index]
    return pass_string

def get_password_requirements():
    min_length = int(input("Enter the minimum password length: "))
    numbers = input("Do you want the password to contain numbers? y/n: ")
    if numbers == "y":
        numbers = True
    else:
        numbers = False
    special_characters = input("Do you want the password to contain special characters? y/n: ")
    if special_characters == "y":
        special_characters = True
    else:
        special_characters = False
    return min_length, numbers, special_characters

def main():
    pass_requirements = get_password_requirements()
    return generate_password(pass_requirements[0], pass_requirements[1], pass_requirements[2])


print(main())
print("hello")
