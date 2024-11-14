# Text Encryption System
This code is a simple user account management system that allows users to create accounts, change usernames and passwords, delete accounts, and display account information stored in a text file. It includes functions for initialising files, managing accounts, and interacting with user data, possibly with options for encryption and decryption. In ensure compatibility across different OS types ('\' for Windows and '/' for others) by automatically assigning the correct directory separator based on the system.

# 
## 1.Account Creation:
 Collects account details such as username, password, email, phone number, and a security question.
 Ensures unique usernames and email addresses.
 Validates password strength (at least 8 characters, including a special character).
 Stores the account data persistently by saving it to a binary file.

## 2.Account Modification:
 Allows users to update the username or password for an existing account.
 Saves any changes made to the binary file, updating the account information persistently.

## 3.Account Deletion:
 Provides a way to remove a specific account by username.
 Updates the stored data after deletion to maintain accuracy.

## 4.Data Retrieval and Display:
 Reads from the binary file and displays the list of all stored accounts when needed.
 
## 5.User Interaction with Menu System:
 A simple menu system prompts users to select different actions, such as creating or deleting an account, updating details, or viewing stored data.
 The program continues to run until the user decides to exit by entering -1.
 
## 6.Encrypting data:
It converts each character into a unique three-digit code according to specific mappings. This way, the original text is transformed into an encoded string of numbers, which can later be stored or transmitted securely.

## 7. Dicrypting data:
The three-digit codes are mapped to corresponding characters, such as uppercase letters, lowercase letters, digits, and special characters, allowing the code to reconstruct the original plaintext message.

# Features-
 1. Create an account.
 2. Change an existing username.
 3. Change the password for an account.
 4. Delete an account.
 5. Display all account information.
 6. Authentication.
 7. Encrypting data.
 8. Dicrypting data.

