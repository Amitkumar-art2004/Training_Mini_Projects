import random
import string
class PasswordError(Exception):
    pass
def generate_password():
    chars =  r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    password = ""
    for i in range(8):
        password += random.choice(chars)
    return password
def validate_password(password):
    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters")
    if not any(char.isdigit() for char in password):
        raise PasswordError("Password must contain a number")
    if not any(char in "@#$%" for char in password):
        raise PasswordError("Password must contain a special character")
    print("Valid Password")
print("Generated Password:", generate_password())

try:
    user_password = input("Enter Password: ")
    validate_password(user_password)

except PasswordError as e:
    print(e)
