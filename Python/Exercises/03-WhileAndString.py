'''
Create a program that asks the user to enter his name and 
replace each character of the name with an asterisk
'''

user_name = input("Enter your name: ")
new_name = ""
index = 0

while index < len(user_name):
    new_name += f'*{user_name[index]}'
    if index == len(user_name) - 1:
        new_name += '*'
    index += 1

print(new_name)
