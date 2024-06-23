import random
import string

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length for your password: "))

# Generate a password using a combination of random characters
# Including lowercase letters, uppercase letters, digits, and punctuation
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_length))

# Display the generated password
print("Generated password:", password)