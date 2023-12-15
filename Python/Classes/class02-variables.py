# VARIABLES IN PYTHON____________________________________

# Declaring and initializing variables
name = "John"
age = 25
is_student = True
pi = 3.14

# Printing the variable values
print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)
print("Pi:", pi)

# Modifying variable values
age = 26
is_student = False
pi = 3.14159

# Printing the modified variable values
print("Updated Age:", age)
print("Updated Is Student:", is_student)
print("Updated Pi:", pi)

# Exercise 1: Variables in Python____________________________________
name_patient = "Donny"
lastname_patient = "Rivera"
age_patient = 40
dob_patient = "13/07/1983"
adult_patient = age_patient >= 18
weight_patient = 103
height_patient = 1.75

print("Name:", name_patient)
print("Last Name:", lastname_patient)
print("Age:", age_patient)
print("DOB:", dob_patient)
print("Adult:", adult_patient)
print("Weight (kg):", weight_patient)
print("Height (m):", height_patient)

# Exercise 2: IMC Calculator_________________________________________
name_imc = input("Enter your name: ")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

imc = weight / (height ** 2)

print(name_imc, "has an weight of", weight, "kg and height of",
      height, "and an IMC of", round(imc, 2))
