'''
Immutables Built-in Functions in Python
'''

user = 'donny'
new_user = f'{user[:3]}inho'
# user[3] = 'a'
print(user[3], new_user)

print(user.capitalize()) # Capitalize
print(user.upper()) # Upper
print(user.lower()) # Lower
print(user.title()) # Title
print(user.swapcase()) # Swapcase


print(user.zfill(10)) # Zfill with 10 zeros