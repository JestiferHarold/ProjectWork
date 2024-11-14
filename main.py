from os_utils import *
from file_utils import *
from  encrypt import *
from decrypt import *
# from os import *
from platform import *
from time import *
from decorator import *

def quit() -> None:
    print("Thank you for using our service")
    exit()

def init():

    option = int(input('''

1. Login
2. Create an account 
3. Forgot Password
4. Exit
                       
'''))
    
    if 0 < option < 5:
        return init_option_match(option)

    clear_terminal()
    print("The option entered is invalid try again")
    sleep(3)
    clear_terminal()
    init()
        
def init_option_match(option):
    sleep(1)
    if str(option) in '1':
        decorator1("Login","Valid Option")
        return asd()
    elif str(option) in '2':    
        decorator1("Account Creation","Valid Option")
        return caa()
    elif str(option) in '3':
        decorator1("Forgot password","Valid Option")
        return forgot_password()
    else:
        decorator_for_quiting("Quiting")
        return quit()

def asd() -> None:
    global asdname1
    asdname1 = input("Enter your username : ")
    password = input(f"Enter the password for {asdname1} : ")
    basic_decorator()
    if login(asdname1, password):
        
        global logged_user
        logged_user = asdname1
        decorator1("Dashboard", "Login in successfull")
        return Dashboard()
    
    else:

        print("Password or username is wrong, please try again")
        basic_decorator()
        asd()


def forgot_password():
    username = input("Enter your username : ")
    email = input("Enter your email : ")
    basic_decorator()

    if check_if_email_and_username_match(username, email):

        print(f"Username {username} with {email} as email exists")
        new_password = input(f"Enter the new password for {username} : ")
        change_password_forgot(username, new_password)
        decorator1("Login",f"Password for {username} has been changed")
        return login()
    
    print("Invaild username and email, Try again")
    basic_decorator()
    forgot_password()

def caa() -> None:
    asdname = input("Enter your username : ")
    password = input(f"Enter the password for {asdname} : ")
    email = input(f"Enter the email for {asdname} : ")
    basic_decorator()

    if create_account(asdname, password, email):
        decorator1("Main Page",f"An account with the username {asdname} and email {email} has been created")
        return init()
    
    print(f"Account with the username {asdname} exist, try an different username")
    basic_decorator()
    caa()

def daa():
    asdname = input("Enter your username : ")
    basic_decorator()
    if check_if_username_exists(asdname):
        def decoy():
            password = input(f"An account with the username {asdname} exist enter password to proceed : ")
            if is_password_same(asdname, password):
                delete_directory(asdname)
                decorator1("Account Settings",f"The Account with the username {asdname} has been deleted")
                return account_settings()
            basic_decorator()
            print("Wrong password")
            return decoy()
        return decoy()
    
    print(f"Account with the username {asdname} does not exist.")
    basic_decorator()
    init()

def Dashboard():
    options2 = int(input('''
Welcome to the Dashboard, select an option to move forward
                         
1. Create and encrypt data
2. decrypt an encrpyted data
3. Delete an file
4. Account options
5. Logout

Enter your option HERE : '''))
    
    if 0 < options2 < 6:
        return Dashboard_comb(options2)
    
    basic_decorator()
    print("Invaild option, Try again")
    Dashboard()

def Dashboard_comb(i):
    if i == 1:
        decorator1("Encryption","Valid option")
        return encrpyting()
    elif i == 2:
        decorator1("Decryption","Valid option")
        return decrpyt()
    elif i == 3:
        decorator1("File Detetion","Valid option")
        delete_em()
    elif i == 4:
        decorator1("Account Settings","Valid option")
        account_settings()
    else:
        decorator_for_quiting("Logging out of")
        return quit()
    
def account_settings():
    opt = int(input('''
1. Delete Account and it's data
2. Change Password
3. Change Username
4. Go Back
5. Logout'''))
    
    if 0 < opt < 6:
        return account_settings_comb(opt)
    
    basic_decorator()
    print("Invalid option Try again")
    account_settings()

def inv_pass():
    username = input("Enter your username : ")
    old_password = input("Enter your old password : ")
    new_password = input("Enter your new Password : ")
    basic_decorator()
    if change_password(username, old_password, new_password):
        if password_strength(new_password):
            basic_decorator()
            inv_pass()
        print(f"The password for {username} has been changed.")
        return account_settings()
    basic_decorator()
    print("Password or username incorrect")
    inv_pass()

def inv_user():
    password = input("Enter your password : ")
    basic_decorator()
    if is_password_same(asdname1, password):
        new_username = input("Enter your new username : ")
        change_username(asdname1, password, new_username)
        print("Username has been changed successfully ")
        return account_settings()
    basic_decorator()
    return inv_user()
        

def account_settings_comb(opt):
    if opt == 1:
        decorator1("Account Deletion","Valid option")
        return daa()
    elif opt == 2:
        decorator1("Password Changing","Valid option")     
        return inv_pass()
    elif opt == 3:
        decorator1("Username Changing","Valid option")
        return inv_user()
    elif opt == 4:
        decorator1("Dashboard","")
        return Dashboard()
    else:
        decorator_for_quiting("Logging out of")
        return quit()

def encrpyting():
    data = input("Enter data which is to be encrypted \n")
    file_name = input("Enter the file name : ")
    basic_decorator()
    if file_name not in list_all_files(logged_user):
        data1 = texties(data)
        print(type(asdname1))  # Check the type of asdname1
        print(type(file_name))
        print(type(logged_user))
        # print(sep)
        with open(f'Accounts{os.sep}{str(asdname1)}{os.sep}{str(file_name)}.txt', 'w+') as g:
            g.write(data1)
        decorator1("Dashboard",f"The data has been encrypted and has been saved in a file name {file_name}")
        return Dashboard()
    basic_decorator()
    print(f"file with the name {file_name} exists, try again")
    encrpyting()

def decrpyt():
    file_name = input("Enter the name of the file")
    basic_decorator()
    if file_name in list_all_files(asdname1):
        data = read_encrypted_file(asdname1, file_name)
        m = fuck(data)
        print("The decrpyted message is \n", m)
        basic_decorator()
        return Dashboard()
    
    print(f"encrypted file with the name {file_name} is not avaialble, try again")
    basic_decorator()
    decrpyt()

def delete_em():
    file_name = input("Enter the name of the file you want to delete")
    basic_decorator()
    if file_name in list_all_files(logged_user):
        remove_file(asd, file_name)
        decorator1("Dashboard",f"{file_name} has been removed successfully from your account")
        return Dashboard()
    
    
    print(f"encrypted file with the name {file_name} is not avaialble, try again")
    basic_decorator()
    delete_em()

clear_terminal()
print("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\tWELCOME TO TEXT ENCRYPTION SYSTEM ")
sleep(2)
clear_terminal()

keys = list(dict.keys(dict1))
check_if_all_directories_exists(keys)
init()