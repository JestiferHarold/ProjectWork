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

def delete_directory(name : str) -> None:
    '''deletes the directory with the argument passed '''

    rmtree('Accounts' + sep + name) 

def check_if_all_directories_exists(name_list : list) -> None:
    '''Checks if all the directories for the accounts are present
                                   if not creates a new directory for it''' 
    for name in name_list:
        if not os.path.exists("Accounts" + sep + name):
            create_directory(name)
    

def create_encrypted_file(account , data , file2 ) -> None:

    m = 'Accounts' + '\\' + account + '\\' + file2 + '.txt'
    print(m)
    with open(file2 + '.txt', 'w+') as g:
        g.write(data)

def list_all_files(way) -> list:

    m = listdir('Accounts' + sep + way)
    return m
def delete_a_file(name : str) -> None:
    
    remove('Accounts' + sep + name)

def read_encrypted_file(username : str, file2) -> None:
    with open('Accounts' + sep + username + sep + file2, 'r') as g:
        return g.read()

def remove_file(username : str, file_name : str) -> None:
    remove('Accounts' + sep + username + sep + file_name)
    
