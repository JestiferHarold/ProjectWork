from pickle import *
from os_utils import *
from os import path
from copy import *
import re

global dict1
dict1 = {}
m = 0

def binary_flush():

    dump(dict1, file)
    file.flush()

def password_strength(pswd):

    char = r'[^a-zA-Z0-9\s]'
    if (bool(re.search(char, pswd))) and len(pswd) >= 8:
        print("Strong password")
        return False
    elif (bool(re.search(char, pswd))) and len(pswd) < 8:
        print('Password should contain atleast 8 characters.')
        return True
    elif (not(bool(re.search(char, pswd)))) and len(pswd) >= 8:
        print("Password should contain atleast one special character.")
        return True

def check_if_username_exists(username):
     
    if username in DICT:
        return True


def check_if_email_exists(email):

    for key in DICT:
        if email == (DICT[key][1]):
            print("{0} email already exists.".format(email))
            return True  
                             

def check_if_binary_file_exists():
    return path.exists("credentials.bin")


def create_base_binary_file():
    if not check_if_binary_file_exists():
        with open("cred.dat","wb+") as what:
            ...

def is_password_same(username, password) -> bool:
    if dict1[username][0] == password:
        return True

def open_binary_file():
    global file
    file = open("cred.bin","ab+")
    binary_flush()

def read_binary_file():
    dict1 = load(file)

def binary_flush():
    dump(dict1, file)
    file.flush()

def login(username, password):
    if username in dict1 and dict1[username][0] == password:
        return True
    else:
        return False

 
def create_account(username, password, email):
    if not check_if_username_exists(username) and check_if_email_exists(email) and not password_strength(password):
        dict1[username] = [password, email]
        binary_flush()
        read_binary_file()
        return True

def delete_account(username, password):
    if check_if_username_exists(username) and password :
        del dict1[username]
        binary_flush()
        read_binary_file()

def change_password(username, old_password, new_password):
    if check_if_username_exists(username) and old_password == dict1[username][0]:
        dict1[username][0] = new_password
        binary_flush()
        read_binary_file()

def change_username(username, password, new_username):
    if check_if_username_exists(username) and password == dict1[username][0] and not check_if_username_exists(new_username):
        m = copy(dict1[username])
        del dict1[username]
        dict1[new_username] = copy(m)
        binary_flush()
        read_binary_file()

def change_email(username, password, new_email):
    if check_if_username_exists(username) and password == dict1[username][0]:
        dict1[username][2] = new_email
        binary_flush()
        read_binary_file()


functions_list = [
    # director_seperator,
    # create_directory,
    # delete_directory,
    # check_if_all_directories_exists,
    # password_strength,
    # check_if_email_exists,
    # final_directory,
    # check_if_username_exists,
    # create_base_binary_file,
    # create_account,
    # read_binary_file,
    # delete_account,
    # change_password,
    # change_username
]