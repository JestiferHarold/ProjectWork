from os_utils import *
from file_utils import *
from  encrypt import *
from decrypt import *
from platform import *
from time import *
from decorator import *

def quit() -> None:

    '''Quits the program'''

    print("Thank you for using our service")
    exit()

def init() -> None:

    '''This is the main function '''
    
    m = list(dict.keys(dict1))
    check_if_all_directories_exists(m)
    option = int(input('''
Welcome to the Text Encryption Program

1. Login
2. Create an account 
3. Forgot Password
4. Exit
                       
Enter an option HERE to move forward : '''))
    
    if 0 < option < 5:
        return init_option_matcher(option)

    clear_terminal()
    print("The option entered is invalid try again")
    sleep(3)
    clear_terminal()
    init()
        
def init_option_matcher(option : int) -> None:

    '''This function matches the function to the option given as an argument'''
    
    sleep(1)
    if str(option) in '1':
        decorator1("Login","Valid Option")
        return logging()
    elif str(option) in '2':    
        decorator1("Account Creation","Valid Option")
        return creating_an_account()
    elif str(option) in '3':
        decorator1("Forgot password","Valid Option")
        return forgot_password()
    else:
        decorator_for_quiting("Quiting")
        return quit()

def logging() -> None:

    '''This function allows you to input username and password to login into you account'''

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
        logging()


def forgot_password() -> None:

    '''This function allows you to reset the password using username and email'''

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

def creating_an_account() -> None:

    '''This function is used to create an account with a password and an email attached to it'''

    asdname = input("Enter your username : ")
    password = input(f"Enter the password for {asdname} : ")
    email = input(f"Enter the email for {asdname} : ")
    basic_decorator()

    if create_account(asdname, password, email):
        decorator1("Main Page",f"An account with the username {asdname} and email {email} has been created")
        return init()
    
    print(f"Account with the username {asdname} exist, try an different username")
    basic_decorator()
    creating_an_account()

def deleting_an_account() -> None:

    '''This function is used to delete an account and it's data from the secondary storage device'''

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

def Dashboard() -> None:

    '''This function can be used as the dashboard and will provide option to proceed forward'''

    options2 = int(input('''
Welcome to the Dashboard, select an option to move forward
                         
1. Create and encrypt data
2. decrypt an encrpyted data
3. Delete an file
4. Account options
5. Logout

Enter your option HERE : '''))
    
    if 0 < options2 < 6:
        return Dashboard_option_matcher(options2)
    
    basic_decorator()
    print("Invaild option, Try again")
    Dashboard()

def Dashboard_option_matcher(i : int) -> None:

    '''This function is used to map to a function according to the parameter passed'''

    if i == 1:
        decorator1("Encryption","Valid option")
        return encrpyting()
    elif i == 2:
        decorator1("Decryption","Valid option")
        return decrpyting()
    elif i == 3:
        decorator1("File Detetion","Valid option")
        deleting_files()
    elif i == 4:
        decorator1("Account Settings","Valid option")
        account_settings()
    else:
        decorator_for_quiting("Logging out of")
        return quit()
    
def account_settings() -> None:

    '''This function is used for accessing the account settings like deletion, password managemnt, etc'''

    opt = int(input('''
Account Settings, select an option to move forward
                    
1. Delete Account and it's data
2. Change Password
3. Change Username
4. Go Back
5. Logout
                    
Enter your option HERE : '''))
    
    if 0 < opt < 6:
        return account_settings_option_matcher(opt)
    
    basic_decorator()
    print("Invalid option Try again")
    account_settings()

def inv_pass() -> None:

    '''This function is used to set an new password for an account'''

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

def inv_user() -> None:

    '''This function is used to set an new username for an account'''

    password = input("Enter your password : ")
    basic_decorator()
    if is_password_same(asdname1, password):
        new_username = input("Enter your new username : ")
        change_username(asdname1, password, new_username)
        print("Username has been changed successfully ")
        return account_settings()
    basic_decorator()
    return inv_user()
        

def account_settings_option_matcher(opt : int) -> None:

    '''This function is used to match the desired options with the parameters passed'''

    if opt == 1:
        decorator1("Account Deletion","Valid option")
        return deleting_an_account()
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

def encrpyting() -> None:

    '''This function is used for encrypting data to numbers and save it in a file'''

    data = input("Enter data which is to be encrypted : ")
    file_name = input("Enter the file name : ") 
    basic_decorator()
    if file_name not in list_all_files(logged_user):
        data1 = texties(data)
        create_encrypted_file(asdname1, file_name, data1)
        decorator1("Dashboard",f"The data has been encrypted and has been saved in a file name {file_name}")
        return Dashboard()
    basic_decorator()
    print(f"file with the name {file_name} exists, try again")
    encrpyting()

def decrpyting() -> None:

    '''This function is used for decrypting encryted data'''

    file_name = input("Enter the name of the file : ")
    basic_decorator()
    if file_name in list_all_files(asdname1):
        data = read_encrypted_file(asdname1, file_name)
        m = decrypt(data)
        print("The decrpyted message is \n", m)
        if not input("\nPress enter to get back to the Dashboard : "):
            basic_decorator()
            return Dashboard()

    print(f"encrypted file with the name {file_name} is not avaialble, try again")
    basic_decorator()
    decrpyting()

def deleting_files() -> None:

    '''This function is used for deleting files from a certain account'''

    file_name = input("Enter the name of the file you want to delete : ")
    basic_decorator()
    if file_name in list_all_files(logged_user):
        remove_file(logged_user, file_name)
        decorator1("Dashboard",f"{file_name} has been removed successfully from your account")
        return Dashboard()
    
    
    print(f"encrypted file with the name {file_name} is not avaialble, try again")
    basic_decorator()
    deleting_files()

clear_terminal()
print("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\tWELCOME TO TEXT ENCRYPTION SYSTEM ")
sleep(2)
clear_terminal()
m = list(dict.keys(dict1))
check_if_all_directories_exists(m)
init()