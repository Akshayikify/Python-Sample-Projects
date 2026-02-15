import random
import string

def generate_password(username, length):

    # Character sets
    digits = string.digits
    symbols = "!@#$%^&*"

    # Step 1: Use part of the username
    username_part = username[:4] if len(username) >= 4 else username

    # Step 2: Add mandatory characters
    password_chars = list(username_part)
    password_chars.append(random.choice(string.ascii_uppercase))
    password_chars.append(random.choice(digits))
    password_chars.append(random.choice(symbols))

    # Step 3: Fill remaining length with random characters
    all_chars = string.ascii_letters + digits + symbols
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    # Step 4: Shuffle to avoid predictable pattern
    random.shuffle(password_chars)

    # Step 5: Join as string
    return "".join(password_chars)


# -------- Main Program --------
username = input("Enter username: ")
password_length = int(input("Enter password length (>=8): "))

password = generate_password(username, password_length)
print("Generated Password:", password)
