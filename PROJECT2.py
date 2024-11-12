import os
from import * 
import pickle
import re


DICT={}
file= open("draftfile.bin","ab") 
pickle.dump(DICT,file)


def password_strength(pswd):
    char=r'[^a-zA-Z0-9\s]'
    if (bool(re.search(char, pswd))) and len(pswd)>=8:
        print("Strong password")
        return False
    elif (bool(re.search(char, pswd))) and len(pswd)<8:
        print('Password should contain atleast 8 characters.')
        return True
    elif (not(bool(re.search(char, pswd)))) and len(pswd)>=8:
        print("Password should contain atleast one special character.")
        return True

    ...

def check_if_username_exists(username):
    if username in DICT:
        print("Username already exists.")
        return True
    else:
        return False

    ...


def check_if_email_exists(email):
    for key in DICT:
        if email==(DICT[key][1]):
            print("{0} email already exists.".format(email))
            
            return True  
                                                          #gotta include break here somehow
        else:
            return False

    ...




def read_binary_file():
    with open("draftfile.bin","rb") as file:
        content=pickle.load(file)
        print(content)

def create_account():                              
    username=input("Enter username:")
    pswd=input("Enter password:")
    email=input("Enter emailid:")
    phn_number=int(input('Enter phone number:'))
    security_qn=input("Enter security question:")

    while check_if_username_exists(username):   
        username=("Enter alternate username:")
        continue

    while check_if_email_exists(email):
        email=input("Enter alternate email:")
        continue

    while password_strength(pswd):
        pswd=input("Enter alternate pswd:")
        continue

    else:
        DICT[username]=(pswd,email,phn_number,security_qn)
        pickle.dump(DICT,file)  #function needs to be called again. wouldnt it be better to not put 'createfile' inside a function.
        read_binary_file()
            
    ...

def delete_account(username):
    if username in DICT:
        del DICT[username]
        pickle.dump(DICT,file)
        print(username," account successfully deleted.")

    else:
        print(username," username doesnt exist.")
    print("Current directory : ",read_binary_file)

    ...

def change_password(pswd,username):
    if username in DICT:
        DICT[username][1]=pswd
        pickle.dump(DICT,file)
        print("Password successfully updated.")
    else:
        print(username, "username doesnt exist.")
    ...

def change_username(username,newusername):
    if username in DICT:
        DICT[newusername]=DICT[username]
        del DICT[username]
        pickle.dump(DICT,file)
        print(username,"username successfully changed.")
    else:
        print(username,"username doesnt exist.")
    ...



print("1. Create Account","\n","2. Change username",'\n',"3. Change password","4. Delete account.","\n","5. Display file")
choice=0
while choice!=-1:
    choice=int(input("Enter your choice (-1 to exit):"))
    if choice==1:
        create_account()
    elif choice==2:
        change_username()
    elif choice==3:
        change_password()
    elif choice==4:
        delete_account()
    elif choice==5:
        read_binary_file()






file.close()