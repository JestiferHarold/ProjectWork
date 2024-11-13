from pickle import *
from os_utils import *
from os import *
import re

def create_base_binary_file():
    if not path.exists("credentials.bin"):
        with open("credentials.bin","xb") as file:
            pass

DICT={}


def password_strength(pswd):
    pswd = input("Enter password:")
    char = r'[^a-zA-Z0-9\s]'
    if (bool(re.search(char, pswd))) and len(pswd)>=8:
        print("Strong password")
    elif (bool(re.search(char, pswd))) and len(pswd)<8:
        print('Password should contain atleast 8 characters.')
    elif (not(bool(re.search(char, pswd)))) and len(pswd)>=8:
        print("Password should contain atleast one special character.")

    ...

def check_if_username_exists(username : str) -> None:
    if username in DICT:
        print("Username already exists.")
        return None


def check_if_email_exists(email):

    for key in DICT:

        if email==(DICT[key][1]):
            print("{} email already exists.".format(email))
            return True
                                                          #gotta include break here somehow
        else:
            return False

    ...




def read_binary_file():
    global file
    file = open("wtf.bin","wb")

def create_account():
    username=input("Enter username:")
    pswd=input("Enter password:")
    email=input("Enter emailid:")
    phn_number=int(input('Enter phone number:'))
    security_qn=input("Enter security question")
    while check_if_username_exists(username):   
        username=("Enter username:")
        continue


      
       
        
    else:
        DICT[username]=(pswd,email,phn_number,security_qn)
        dump(DICT,file)

            
    ...

def delete_account():
    ...

def change_password():
    ...

def change_username():
    ...