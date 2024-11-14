import os
from os import path
import platform
from shutil import *    
from sys import path
from file_utils import *
from time import *

def get_os_name():

    '''returns the name of the operating system'''

    return platform.system()

def clear_terminal():

    '''Clears the terminal'''

    if get_os_name() in ("Windows",'asd'):
        return os.system("cls")
    
    return os.system("clear")

def create_directory(name : str) -> None:

    '''Creates a directory with the argument passed'''

    os.mkdir('Accounts' + os.sep + name)

def delete_directory(name : str) -> None:

    '''deletes the directory with the argument passed '''

    rmtree('Accounts' + os.sep + name) 

def check_if_all_directories_exists(name_list : list) -> None:

    '''Checks if all the directories for the accounts are present
                                   if not creates a new directory for it''' 
    
    for name in name_list:
        if not os.path.exists("Accounts" + os.sep + name):
            create_directory(name)
    

def create_encrypted_file(account : str , file2 : str , data : str ) -> None:

    '''Creates an text file and addes encrypted data'''

    with open(f'Accounts' + os.sep + account + os.sep + file2 + '.txt', 'w+') as g:
            g.write(data)
    

def list_all_files(way) -> list:

    return os.listdir('Accounts' + os.sep + way)

def read_encrypted_file(username : str, file2 :str) -> None:

    '''Reads an encrypted file'''

    with open('Accounts' + os.sep + username + os.sep + file2, 'r') as g:
        return g.read()

def remove_file(username : str, file_name : str) -> None:

    '''Removes a file of a folder '''
    
    os.remove('Accounts' + os.sep + username + os.sep + file_name)
    
def change_directory_name(old_name, new_name):
    
    '''Changes the name of the folder'''

    os.rename('Accounts' + os.sep + old_name, 'Accounts' + os.sep + new_name)