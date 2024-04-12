import random
#choose whether or not password should contain special characters
#choose minimum password length
#choose whether or not password should contain numbers
def password_generator(min_length, special_characters, numbers):
    password = ""
    extra_characters = 0
    keep_going = True
    while keep_going:
        yes_no = random.randint(0,1)
        if yes_no == 0:
            keep_going = False
        else:
            extra_characters += 1
    pass_length = min_length + extra_characters
    #return pass_length

    #lower_letters_dict = {}
    #upper_letters_dict = {}
    #numbers_dict = {}
    #special_characters_dict = {}
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    #Symbols not yet supported
    while pass_length > 0:
        character_group = random.randint(0,2)
        if character_group == 0:
            group_index = random.randint(0, len(lower_letters) - 1)
            password += lower_letters[group_index]
        elif character_group == 1:
            group_index = random.randint(0, len(lower_letters) - 1)
            password += lower_letters[group_index].upper()
        else:
            group_index = random.randint(0, 9)
            password += str(group_index)
        pass_length -= 1
    return password


#Test
print(password_generator(12, True, True))

