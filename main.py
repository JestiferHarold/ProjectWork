from os_utils import *
from tkinter_utiks import *
from file_utils import *
from PROJECT import *
from os import *
from time import *

def init() -> None:
    open_binary_file()
    read_binary_file()
    while True:
        option = int(input('''
1. Login
2. Create an account 
3. Delete an account
'''))
        
def asd() -> None:
    global asdname1
    asdname1 = input("Enter your username : ")
    password = input(f"Enter the password for {asdname1} : ")
    if login(asdname1, password):
        print("Login in successfull")
        global asd
        asd = asdname1
        return 
    else:
        print("Password or username is wrong, please try again")
        time(10)
        asd()
    

def caa() -> None:
    asdname = input("Enter your username : ")
    password = input(f"Enter the password for {asdname} : ")
    email = input(f"Enter the email for {asdname} : ")
    if create_account(asdname, password, email):
        print(f"An account with the username {asdname} and email {email} has been created")
        time(10)

        return 
    else:
        print(f"Account with the username {asdname} exist, try an different username")
        time(10)
        caa()

def daa():
    asdname = input("Enter your username : ")
    if check_if_username_exists(asdname):
        def decoy():
            password = input(f"An account with the username {asdname} exist enter password to proceed : ")
            if is_password_same(asdname, password):
                delete_directory(asdname)
                print(f"The Account with the username {asdname} has been deleted")
                return 
            print("Wrong password")
            decoy()
    else:
        print(f"Account with the username {asdname} does not exist.")
        init()

def options():
    options2 = int(input('''
1. Create and encrypt data
2. decrypt an encrpyted data'''))



def fillie():
    data = input("Enter data which is to be encrypted \n")
    file_name = input("Enter the file name : ")
    if file_name not in list_all_files():
        ...


create_base_binary_file()
init()