import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# --- KEY MANAGEMENT ---

def load_or_create_salt():
    """Ensures a consistent salt is used for the master password."""
    if not os.path.exists("salt.salt"):
        salt = os.urandom(16)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    else:
        with open("salt.salt", "rb") as salt_file:
            salt = salt_file.read()
    return salt

def derive_key(master_password, salt):
    """Turns the master password into a valid 32-byte Fernet key."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

# --- MAIN APP LOGIC ---

master_pwd = input('Enter the master password: ')
salt = load_or_create_salt()
key = derive_key(master_pwd, salt)
fer = Fernet(key)

def view():
    if not os.path.exists('passwordmngr.txt'):
        print("No passwords saved yet.")
        return
        
    with open('passwordmngr.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" not in data: continue
            
            name, encrypted_pwd = data.split('|')
            try:
                decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
                print(f'User: {name} | Password: {decrypted_pwd}')
            except Exception:
                print(f'User: {name} | [Error: Wrong master password or corrupted data]')

def add(): 
    name = input('Enter your account name: ')
    paswd = input('Enter your password: ')
    with open('passwordmngr.txt', 'a') as f:
        encrypted_pwd = fer.encrypt(paswd.encode()).decode()
        f.write(f'{name}|{encrypted_pwd}\n')

# --- EXECUTION LOOP ---

while True:
    mode = input('\nDo you want to add or view passwords? (add/view/quit): ').lower()
    if mode == 'view':
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Invalid mode.")