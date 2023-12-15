# try/catch Introduction____________________________________________
# try: run the code
# except: handle the exception
#

number_str = input("Enter a number: ")

try:
    number_float = float(number_str)
    print(f'Float: {number_float}')
    print(f'The double of {number_str} is {number_float * 2:.2f}')
except:
    print(f"{number_str} is not a number")