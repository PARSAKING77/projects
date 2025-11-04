import re
import sqlite3

# Create a new database and table
conn = sqlite3.connect('user_database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        print("Invalid email format. Please enter a valid email address.")
        return False

def validate_password(password):
    if re.match(r'^(?=.*[a-zA-Z])(?=.*[0-9]).*$', password):
        return True
    else:
        print("Invalid password format. Please enter a password with at least one letter and one number.")
        return False

def store_credentials(email, password):
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (email, password))
    conn.commit()

while True:
    email = input("Enter your email address: ")
    if validate_email(email):
        password = input("Enter your password: ")
        if validate_password(password):
            store_credentials(email, password)
            print("Credentials stored successfully!")
            break
    else:
        continue