from pickle import dump, load
from os_utils import *
import os
from copy import *
import re
from decrypt import *
from encrypt import *
from decorator import *

file1 = None
global dict1
dict1 = {}
m = 0

def binary_flush():
    file1.seek(0)
    dump(dict1, file1)
    file1.flush()

def password_strength(pswd):

    char = r'[^a-zA-Z0-9\s]'
    if (bool(re.search(char, pswd))) and len(pswd) >= 8:
        return True
    elif (bool(re.search(char, pswd))) and len(pswd) < 8:
        return False
    elif (not(bool(re.search(char, pswd)))) and len(pswd) >= 8:
        return False
    


def check_if_username_exists(username):
     
    if username in dict1:
        return True


def check_if_email_exists(email):

    for key in dict1:        
        if email == (dict1[key][1]):
            print("{0} email already exists.".format(email))
            return True  
                             
def check_if_email_and_username_are_the_same(username,email):
    if dict1[username][1] == email:
        return True

def check_if_binary_file_exists():
    return os.path.exists("credentials.bin")

def create_base_binary_file():
    global file1
    if not check_if_binary_file_exists():
        with open("credentials.bin", "wb+") as file1:    #c2
            ...

def is_password_same(username, password) -> bool:
    if dict1[username][0] == password:
        return True

def open_binary_file():
    global file1
    if file1 is None or file1.closed:
        file1 = open("credentials.bin", "rb+")
    read_binary_file()

def read_binary_file():

    '''Load data from file into dict1 if available'''

    global dict1, file1
    try:
        file1.seek(0)
        dict1 = load(file1)
    except EOFError:
        dict1 = {}

def login(username, password):
    if username in dict1 and dict1[username][0] == password:
        return True
    else:
        return False

 
def create_account(username, password, email):
    if not check_if_username_exists(username):
        dict1[username] = [password, email]
        binary_flush()
        read_binary_file()
        return True

def delete_account(username, password):
    if check_if_username_exists(username) and dict1[username][0] == password :
        del dict1[username]
        binary_flush()
        read_binary_file()

def change_password_forgot(username, new_password):
    change_password(username, new_password, None)

def change_password(username, new_password, old_password):
    if check_if_username_exists(username) and (old_password == dict1[username][0] or old_password == None):
        dict1[username][0] = new_password
        binary_flush()
        read_binary_file()
        return True

def change_username(username, password, new_username):
    if check_if_username_exists(username) and password == dict1[username][0] and not check_if_username_exists(new_username):
        dict1[new_username] = dict1[username]
        del dict1[username]
        binary_flush()
        read_binary_file()
        return True

def change_email(username, password, new_email):
    if check_if_username_exists(username) and password == dict1[username][0]:
        dict1[username][1] = new_email        
        binary_flush()
        read_binary_file()

create_base_binary_file()
open_binary_file()
read_binary_file()

# functions_list = [
#     quit,
#     init,
#     init_option_matcher,
#     logging,
#     forgot_password,
#     creating_an_account,
#     deleting_an_account,
#     Dashboard,
#     Dashboard_option_matcher,
#     account_settings,
#     inv_pass,
#     inv_user,
#     account_settings_option_matcher,
#     encrypting,
#     decrypting,
#     deleting_files,
#     create_directory,
#     delete_directory,
#     check_if_all_directories_exists,
#     password_strength,
#     check_if_email_exists,
#     check_if_username_exists,
#     create_base_binary_file,
#     create_account,
#     read_binary_file,
#     delete_account,
#     change_password,
#     change_username,
#     clear_terminal,
#     fun,
#     decrypt,
#     bets1,
#     bets2,
#     git,
#     space,
#     special,
#     texties,
#     decorator1,
#     basic_decorator,
#     decorator_for_quiting
# ]
