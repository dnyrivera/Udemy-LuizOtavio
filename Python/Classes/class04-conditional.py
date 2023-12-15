# if / elif / else _________________________________________________

# data_input = input('Do you want "login" or "logout" the system?')

# if data_input == 'login':
#     print("You did login in the system")
# elif data_input == 'logout':
#     print("You did logout in the system")
# else:
#     print("You don't type login or logout in the options")

condition_01 = False
condition_02 = False
condition_03 = True
condition_04 = False

if condition_01:
    print("condition_01 is True")
elif condition_02:
    print("condition_02 is True")
elif condition_03:
    print("condition_03 is True")
elif condition_04:
    print("condition_04 is True")
else:
    print("All conditions are False")

if 10 == 10:
    print("10 is equal to 10")

print("out of if")


# logic operators in python ________________________________________

# and
entry = input("[E]Entry or [Q]uit?")
password = input("Password:")

correct_password = "123456"

if entry == "E" and password == correct_password:
    print("Welcome")
else:
    print("Wrong password")

# or

entry = input("[E]Entry or [Q]uit?")
password = input("Password:")

correct_password = "123456"

if (entry == "E" or entry == "e") and password == correct_password:
    print("Welcome")
else:
    print("Wrong password")

# not
# used to invert the result of a condition
# True -> False
# False -> True


# in and not in _________________________________________________

# in
# used to check if a value is in a list or not example

my_list = [1, 2, 3, 4, 5]

if 3 in my_list:
    print("3 is in the list")
else:
    print("3 is not in the list")

# not in
# used to check if a value is not in a list or not example
my_list = [1, 2, 3, 4, 5]
if 6 not in my_list:
    print("6 is not in the list")
else:
    print("6 is in the list")