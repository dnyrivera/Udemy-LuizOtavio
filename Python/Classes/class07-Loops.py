'''
While Loop in Python
Execute a block of code as long as a condition is true
'''
condition = True

while condition:
    user = input("Enter your name: ")
    if user == "stop":
        break  # Break the loop when condition is true
    print(f"Hello {user}")

# Count numbers using while loop
count = 0

while count <= 10:
    count += 1  # Increment the count

    if count in [3, 6, 9]:
        continue  # Skip the current iteration

    print(count)

    if count == 8:
        break  # Break the loop when count is 8

print("Done")

# Indent while loop

total_line = 5
total_column = 5
line = 1  # Set line to 1

while line <= total_line:  # Loop until line is less than or equal to total_line
    column = 1  # Reset column to 1

    while column <= total_column:  # Loop until column is less than or equal to total_column
        print(f'{line= } {column= }')
        column += 1  # Increment column

    print('-' * 20)
    line += 1  # Increment line
