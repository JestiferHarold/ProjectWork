from pickle import *
from test import *
from os import path

def password_strength():
    ...

def check_if_username_exists():
    ...

def check_if_email_exists():
    ...



def create_base_binary_file():
    # if not path.exists("credentials.bin"):
    with open("cred.dat","wb+") as what:
        k = 8   

def read_binary_file():
    file = open("wtf.bin","wb+")

def create_account():
    ...

def delete_account():
    ...

def change_password():
    ...

def change_username():
    ...

functions_list = [
    director_seperator,
    create_directory,
    delete_directory,
    check_if_all_directories_exists,
    password_strength,
    check_if_email_exists,
    final_directory,
    check_if_username_exists,
    create_base_binary_file,
    create_account,
    read_binary_file,
    delete_account,
    change_password,
    change_username
]