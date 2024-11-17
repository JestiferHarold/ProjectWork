from file_utils import *
from os_utils import *
from  encrypt import *
from decrypt import *
from platform import *
from time import *
from decorator import *
import getpass
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
    password = getpass.getpass(f"Enter the password for {asdname1} : ")
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

    if check_if_email_and_username_are_the_same(username, email):

        print(f"Username {username} with {email} as email exists")
        new_password = getpass.getpass(f"Enter the new password for {username} : ")
        change_password_forgot(username, new_password)
        decorator1("Main",f"Password for {username} has been changed")
        return init()
    
    print("Invaild username and email, Try again")
    basic_decorator()
    forgot_password()

def creating_an_account() -> None:

    '''This function is used to create an account with a password and an email attached to it'''

    asdname = input("Enter your username : ")
    password = getpass.getpass(f"Enter the password for {asdname} : ")
    email = input(f"Enter the email for {asdname} : ")
    basic_decorator()

    if create_account(asdname, password, email):
        if password_strength(password):
            decorator1("Main Menu",f" An account with the username {asdname} and email {email} has been created")
            return init()        
        print("Password too weak try again")
        basic_decorator()
        creating_an_account()

    print(f"Account with the username {asdname} exist, try an different username")
    basic_decorator()
    creating_an_account()

def deleting_an_account() -> None:

    '''This function is used to delete an account and it's data from the secondary storage device'''

    asdname = input("Enter your username : ")
    basic_decorator()
    if check_if_username_exists(asdname):
        def decoy():
            password = getpass.getpass(f"An account with the username {asdname} exist enter password to proceed : ")
            if is_password_same(asdname, password):
                delete_directory(asdname)
                delete_account(asdname, password)
                decorator1("Main Menu",f"The Account with the username {asdname} has been deleted")
                return init()
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
        return encrypting()
    elif i == 2:
        decorator1("Decryption","Valid option")
        return decrypting()
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
    old_password = getpass.getpass("Enter your old password : ")
    new_password = getpass.getpass("Enter your new Password : ")
    basic_decorator()
    if change_password(username, old_password, new_password):
        if password_strength(new_password):
            basic_decorator()
            inv_pass()
        decorator1("Accounts Settings",f"The password for {username} has been changed.")
        return account_settings()
    basic_decorator()
    print("Password or username incorrect")
    inv_pass()

def inv_user() -> None:

    '''This function is used to set an new username for an account'''

    password = getpass.getpass("Enter your password : ")
    basic_decorator()
    if is_password_same(logged_user, password):
        new_username = input("Enter your new username : ")
        if check_if_username_exists(new_username):
            decorator1("Account settings", "Username Already exists try again")
            return account_settings()
        change_username(logged_user, password, new_username)
        change_directory_name(logged_user, new_username)
        decorator1("Accounts Settings","Username has been changed successfully ")
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

def encrypting() -> None:

    '''This function is used for encrypting data to numbers and save it in a file'''

    data = input("Enter data which is to be encrypted : ")
    file_name = input("Enter the file name : ") 
    basic_decorator()
    if file_name not in list_all_files(logged_user):
        data1 = texties(data)
        create_encrypted_file(logged_user, file_name, data1)
        decorator1("Dashboard",f"The data has been encrypted and has been saved in a file name {file_name}")
        return Dashboard()
    basic_decorator()
    print(f"file with the name {file_name} exists, try again")
    encrypting()

def decrypting() -> None:

    '''This function is used for decrypting encryted data'''

    file_name = input("Enter the name of the file : ") + '.txt'
    basic_decorator()
    if file_name in list_all_files(logged_user):
        data = read_encrypted_file(logged_user, file_name)
        d = decrypt(data)
        print("The decrpyted message is \n", d)
        if not input("\nPress enter to get back to the Dashboard : "):
            basic_decorator()
            return Dashboard()

    print(f"encrypted file with the name {file_name} is not avaialble, try again")
    basic_decorator()
    decrypting()

def deleting_files() -> None:

    '''This function is used for deleting files from a certain account'''

    file_name = input("Enter the name of the file you want to delete : ") + ".txt"
    basic_decorator()
    if file_name in list_all_files(logged_user):
        remove_file(logged_user, file_name)
        decorator1("Dashboard",f"{file_name} has been removed successfully from your account")
        return Dashboard()
    
    
    print(f"encrypted file with the name {file_name} is not avaialble, try again")
    basic_decorator()
    deleting_files()

if __name__ == "__main__":
    clear_terminal()
    print("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\tWELCOME TO TEXT ENCRYPTION SYSTEM ")
    sleep(2) 
    clear_terminal()
    m = list(dict.keys(dict1))
    check_if_all_directories_exists(m)
    init()

'''
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star

[Verse 1]
Randorii kyou wa garaaki de lucky day
Kattarii abura yogore mo kore de bye bye
Dare da, dare da, atama no naka yobikakeru koe wa
Are ga hoshii, kore ga hoshii to utatteiru

[Pre-Chorus]
Shiawase ni naritai
Rakushite ikite itai
Kono te ni tsukamitai
Anata no sono mune no naka

[Chorus]
Happy de ume tsukushite
Rest in peace made ikou ze
Itsuka mita jigoku mo ii tokoro
Ai wo baramaite
I love you kenashite kure
Zenbu ubatte waratte kure my honey
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Doryoku, mirai, a bеautiful star
Nanka wasurechatten da
See upcoming rock shows
Get tickets for your favorite artists
You might also like
KICK BACK
米津玄師 (Kenshi Yonezu)
Nobody Gets Me
SZA
Vaundy - CHAINSAW BLOOD (Romanized)
Genius Romanizations
[Refrain]
Doryoku, mirai, a beautiful star
Doryoku, mirai, a bеautiful star
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star

[Verse 2]
Yon, yon, yon, san de hazureru tansansui
Hangurii kojirasete hakisou na jinsei
Yamanai ame wa nai yori saki ni sono kasa wo kure yo
Are ga hoshii, kore ga hoshii
Subete hoshii, tada munashii

[Bridge]
Shiawase ni naritai
Rakushite ikite itai
Zenbu mechakucha ni shitai
Nanimo kamo keshisaritai
Anata no sono mune no naka

[Chorus]
Lucky de ume tsukushite
Rest in peace made ikou ze
Yoi ko dake mukaeru tengoku ja
Doumo ikirannai
I love you kenashite, ubatte
Waratte kure my honey
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Nanka wasurechatten da
[Post-Chorus]
Happy, lucky
Konnichiwa, baby
Yoi ko de itai
Sorya tsumaranai
Happy, lucky
Konnichiwa, baby, so sweet
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Nanka sugoi ii kanji

[Refrain]
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
Doryoku, mirai, a beautiful star
(Ha, ha, ha, ha)
'''
