# Exercise 1: Strings in Python____________________________________
"""
 Ask the user to enter his name and his age
 If name and age was typed correctly : 
    Shows: 
        Your name is {user_name}
        Your inverted name is {user_name}
        Your name have or not space: {user_name_has_space}
        Your name have {number_of_characters} characters
        The first letter of your name is {first_letter_of_name}
        The last letter of your name is {last_letter_of_name}
Else nothing was typed in name or age:
    shows the message: "Sorry you left empty fields"
 """
user_name = input("Enter your name: ")
user_age = input("Enter you age: ")

if (user_name and user_age):
    print(f'Your name is {user_name}')
    print(f'Your inverted name is {user_name[::-1]}')
    if (' ' in user_name):
        print(f'Your name have space')
    else:
        print(f"Your name don't have spaces")
    print(f"Your name have {len(user_name)} characters")
    print(f"The first letter of your name is {user_name[0]}")
    print(f"The last letter of your name is {user_name[len(user_name)-1]}")
else:
    print(f"Sorry, you left empty fields")
