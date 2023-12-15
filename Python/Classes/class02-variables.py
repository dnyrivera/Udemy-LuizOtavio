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

# Constants in Python____________________________________________
speed = 44
car_position = 100

RADAR_1 = 60  # speed of radar 1
RADAR_1_POS = 100  # position of radar 1
RADAR_RANGE = 1  # radar range in meters

fast_car = speed > RADAR_1
car_radar_1_zone = car_position >= (RADAR_1_POS - RADAR_RANGE) and \
    car_position <= (RADAR_1_POS + RADAR_RANGE)
ticket_car = fast_car and car_radar_1_zone

if fast_car:
    print("Car is speeding")
if car_radar_1_zone:
    print("Car is in radar 1 zone")
if ticket_car:
    print("Car was ticketed as speeding in radar 1 zone")

# Flags in Python_________________________________________________
# None = no value / is and is not / id
# True = 1 / False = 0
condition = True
passed_in_the_if = None

if condition:
    passed_in_the_if = True
    print("Entered the if:", passed_in_the_if)
else:
    passed_in_the_if = False
    print("Entered the else", passed_in_the_if)

if passed_in_the_if is None:
    print("Entered the None", passed_in_the_if)
else:
    print("Entered the not None", passed_in_the_if)
