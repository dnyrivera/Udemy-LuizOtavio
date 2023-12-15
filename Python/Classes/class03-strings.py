# f-strings in Python____________________________________________
name = "Alice"
age = 25

# Using format() method to format the string
message = "My name is {} and I am {} years old.".format(name, age)
print(message)

# Using .format() with numbers inside {}
message = "My name is {0} and I am {1} years old.".format(name, age)
print(message)

# Using .format() with named arguments
message = "My name is {nombre} and I am {idade} years old.".format(
    nombre=name, idade=age)
print(message)

# Using f-string to format the string
message = f"My name is {name} and I am {age} years old."
print(message)

# Using f-string and number formatting
variable = 'ABC'
print(f'{variable}')
print(f'{variable:>10}')  # right align
print(f'{variable:<10}')  # left align
print(f'{variable:^10}')  # center align
print(f'{variable:=^10}')  # center align with equal sign)

# number formatting
print(f'{1000.9793789729287:0.4f}')  # 4 decimal places
print(f'{1000.9793789729287:+.4f}')  # + sign for positive numbers
print(f'{1000.9793789729287:0=+10,.4f}')  # + sign for positive numbers with 0 padding

# conversion flags in f-string
print(f'{variable!r}')  # representation

message = f"My name is {name} and I am {age:.4f} years old."
print(message)


# Interpolation____________________________________________________
# %s - string | %d - int | %f - float
# x and X - hexadecimal | o - octal | b - binary
# %c - character | %r - raw string

name = "Alice"
price = 1000.958797
message = "%s's payed $%.2f today" % (name, price)
print(message)

# %04d - adds leading zeros to the number
print("The hexadecimal value of %d is %04X" % (1500,1500))


# Input Function____________________________________________________
number_01 = int(input('Digite um número: '))
numero_02 = int(input('Digite o segundo número: '))

print(f'A soma dos números é : {number_01 + numero_02}')


# String Methods____________________________________________________
# split and join strings
string = "This is a string"
print(string[4:])  # from index 4 to the end
print(string[:4])  # from index 0 to 3
print(string[4:8])  # from index 4 to 7
print(string[::2])  # from index 0 to the end, step 2
print(string[::-1])  # reverse the string

print(len(string))  # length of the string
print(string[0:len(string):2])  # alternate characters
print(string[-1:len(string)*-1:-2])  # reverse the string