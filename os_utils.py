from os import *
import platform
from shutil import *    
from sys import path
from file_utils import *
from time import *

def get_os_name():
    return platform.system()

def clear_terminal():
    if get_os_name() in ("Windows",'asd'):
        return system("cls")
    
    return system("clear")

def director_seperator() -> str:
    '''finds the type of operating system used and 
assigns a directory seperator as per the requirements'''

    if get_os_name() == "Windows":
        return str(chr(92))
    else:
        return "/"
     
def create_directory(name : str) -> None:
    '''Creates a directory with the argument passed'''

    mkdir('Accounts' + director_seperator() + name)

def create_encrypted_file(username, filename):
    with open('Accounts' + director_seperator() + name + director_seperator() + filename, "w") as w:
        pass

def delete_directory(name : str) -> None:
    '''deletes the directory with the argument passed '''

    rmtree('Accounts' + director_seperator() + name) 

def check_if_all_directories_exists(name_list : list) -> None:
    '''Checks if all the directories for the accounts are present
                                   if not creates a new directory for it''' 
    for name in name_list:
        if not path.exists(f"Accounts\\{name}"):
            create_directory(name)
    

def create_encrypted_file(account : str, data : str, file : str) -> None:

    with open('Accounts' + director_seperator() + account + director_seperator() + file, 'w') as g:
        g.write(data)

def list_all_files(way) -> list:

    m = listdir('Accounts' + director_seperator() + way)
    return m
def delete_a_file(name : str) -> None:
    
    remove('Accounts' + director_seperator() + name)

def read_encrypted_file(name : str, file) -> None:
    with open('Accounts' + director_seperator() + name + director_seperator() + file, 'w') as g:
        return g.read()

def remove_file(username : str, file_name : str) -> None:
    remove('Accounts' + director_seperator() + username + director_seperator() + file_name)
    
