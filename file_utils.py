import csv
import os
import re

csv_file_path = "credentials.csv"

# Dictionary to hold user credentials, initialized with sample data
dict1 = {'sanjay': ['asd', 'Sanjay@12'], 'asdada': None}

def initialize_system():
    """Initializes the system by setting up the CSV file and loading existing data."""
    initialize_csv_file()
    load_data_from_csv()

def initialize_csv_file():
    """Creates the CSV file with headers if it doesn't already exist."""
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password", "email"])

def load_data_from_csv():
    """Loads data from CSV file into dict1."""
    global dict1
    dict1 = {}
    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if row:
                    username, password, email = row
                    dict1[username] = [password, email]

def write_data_to_csv():
    """Writes data from dict1 to the CSV file."""
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password", "email"])  # Write header row
        for username, details in dict1.items():
            writer.writerow([username] + details)

def password_strength(password):
    """Checks if the password meets strength requirements."""
    if len(password) < 8:
        print("Password should contain at least 8 characters.")
        return False
    if not re.search(r'[^a-zA-Z0-9\s]', password):
        print("Password should contain at least one special character.")
        return False
    print("Strong password")
    return True

def check_if_username_exists(username):
    """Checks if the username exists in dict1."""
    return username in dict1

def check_if_email_exists(email):
    """Checks if the email exists for any user in dict1."""
    for key, details in dict1.items():
        if details[1] == email:
            print(f"{email} already exists.")
            return True
    return False

def check_if_email_and_username_match(username, email):
    """Checks if the username and email match for an existing user."""
    return dict1.get(username, [None, None])[1] == email

def login(username, password):
    """Verifies if the username and password are correct."""
    return dict1.get(username, [None])[0] == password

def create_account(username, password, email):
    """Creates a new account if username and email are unique and password is strong."""
    if check_if_username_exists(username):
        print("Username already exists.")
        return False
    if check_if_email_exists(email):
        print("Email already exists.")
        return False
    if password_strength(password):
        dict1[username] = [password, email]
        write_data_to_csv()
        print(f"Account created successfully for {username}.")
        return True
    return False

def delete_account(username, password):
    """Deletes the account if the username and password match."""
    if login(username, password):
        del dict1[username]
        write_data_to_csv()
        print(f"Account for {username} deleted successfully.")
        return True
    print("Incorrect username or password.")
    return False

def change_password(username, old_password, new_password):
    """Changes the password if the old password matches and the new password is strong."""
    if login(username, old_password) and password_strength(new_password):
        dict1[username][0] = new_password
        write_data_to_csv()
        print("Password changed successfully.")
        return True
    print("Password change failed.")
    return False

def change_username(username, password, new_username):
    """Changes the username if the password is correct and the new username is unique."""
    if login(username, password) and not check_if_username_exists(new_username):
        dict1[new_username] = dict1.pop(username)
        write_data_to_csv()
        print("Username changed successfully.")
        return True
    print("Username change failed.")
    return False

def change_email(username, password, new_email):
    """Changes the email if the password is correct and the new email is unique."""
    if login(username, password) and not check_if_email_exists(new_email):
        dict1[username][1] = new_email
        write_data_to_csv()
        print("Email changed successfully.")
        return True
    print("Email change failed.")
    return False

# Initialize the system on startup
initialize_system()
