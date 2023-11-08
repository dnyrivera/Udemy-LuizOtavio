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
message = f"My name is {name} and I am {age:.4f} years old."
print(message)

# Input Function____________________________________________________
number_01 = int(input('Digite um número: '))
numero_02 = int(input('Digite o segundo número: '))

print(f'A soma dos números é : {number_01 + numero_02}')
