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

def create_directory(name : str) -> None:
    '''Creates a directory with the argument passed'''

    mkdir('Accounts' + sep + name)

def create_encrypted_file(username, filename):
    with open('Accounts' + sep + name + sep + filename, "w") as w:
        pass

def delete_directory(name : str) -> None:
    '''deletes the directory with the argument passed '''

    rmtree('Accounts' + sep + name) 

def check_if_all_directories_exists(name_list : list) -> None:
    '''Checks if all the directories for the accounts are present
                                   if not creates a new directory for it''' 
    for name in name_list:
        if not path.exists("Accounts" + sep + name):
            create_directory(name)
    

def create_encrypted_file(account : str, data : str, file : str) -> None:

    with open('Accounts' + sep + account + sep + file, 'w') as g:
        g.write(data)

def list_all_files(way) -> list:

    m = listdir('Accounts' + sep + way)
    return m
def delete_a_file(name : str) -> None:
    
    remove('Accounts' + sep + name)

def read_encrypted_file(name : str, file) -> None:
    with open('Accounts' + sep + name + sep + file, 'w') as g:
        return g.read()

def remove_file(username : str, file_name : str) -> None:
    remove('Accounts' + sep + username + sep + file_name)
    
