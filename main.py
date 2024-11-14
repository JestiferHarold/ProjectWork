from os_utils import *
from tkinter_utiks import *
from file_utils import *
# from PROJECT import *
from os import *
from time import *

def quit() -> None:
    print("Thank you for using our service")
    exit()

def init() -> None:
    openn_binary_file()
    read_binary_file()
    option = int(input('''
1. Login
2. Create an account 
3. Delete an account
4. Exit
'''))
    
    if 0 < option < 5:
        init_comb(option)
        return
    
    init()
        
def init_comb(option):
    if option in 1:
        asd()
    elif option in 2:
        caa()
    elif option in 3:
        daa()
    else:
        quit()

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


def forgot_password():
    username = input("Enter your username : ")
    email = input("Enter your email : ")
    if check_if_email_and_username_are_the_same(username, email):
        print(f"Username {username} with {email} as email exists")
        new_password = input(f"Enter the new password for {username} : ")
        change_password_forgot(username, new_password)
        print(f"Password for {username} has been changed")
        return 
    print("Invaild username and email")
    forgot_password()

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
        decoy()
    else:
        print(f"Account with the username {asdname} does not exist.")
        init()

def options():
    options2 = int(input('''
1. Create and encrypt data
2. decrypt an encrpyted data
3. Delete an file
4. Account options
5. Exit'''))
    if 1 < options2 < 5:
        options_comb(options)
        return
    options()

def options_comb(i):
    if i == 1:
        fillie()
    elif i == 2:
        decrpyt()
    elif i == 3:
        ...
    else:
        quit()
    
def account_settings():
    opt = int(input('''
1. Delete Account and it's data
2. Change Password
3. Change Username
4. Go Back
5. Logout'''))
    if 0 < opt < 6:
        account_settings_comb(opt)
        return
    print("Invalid option Try again")
    account_settings()

def inv_pass():
    username = input("Enter your username : ")
    old_password = input("Enter your old password : ")
    new_password = input("Enter your new Password : ")
    if change_password(username, old_password, new_password):
        print(f"The password for {username} has been changed.")
        return account_settings()
    print("Password or username incorrect")
    inv_pass()

def inv_user():
    password = input("Enter your password : ")
    if is_password_same(asdname1, password):
        new_username = input("Enter your new username : ")
        change_username(asdname1, password, new_username)
        print("Username has been changed successfully ")
        return
    return inv_user()
        

def account_settings_comb(opt):
    if opt == 1:
        daa()
    elif opt == 2:
        inv_pass()
    elif opt == 3:
        inv_user()
    elif opt == 4:
        return options()
    else:
        quit()

def fillie():
    data = input("Enter data which is to be encrypted \n")
    file_name = input("Enter the file name : ")
    if file_name not in list_all_files(asdname1):
        ...
    
def decrpyt():
    file_name = input("Enter the name of the file")
    if file_name in list_all_files(asdname1):
        ...
    
def delete_em():
    file_name = input("Enter the name of the file you want to delete")
    if file_name in list_all_files(asdname1):
        remove_file(asdname1, file_name)
        print(f"{file_name} has been removed successfully from your account")
        return
    print(f"encrypted file with the name {file_name} is not avaialble, try again")
    time(10)
    delete_em()


create_base_binary_file()
init()