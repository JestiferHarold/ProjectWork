from os import *
from platform import *
from shutil import *    
from sys import path
from file_utils import *


def director_seperator() -> str:
    '''finds the type of operating system used and 
assigns a directory seperator as per the requirements'''

    dir_sep = system()

    if dir_sep.startswith("Wind"):
        return "\\"
    else:
        return "/"

def final_directory(name : str) -> str:

    return director_seperator() +  'students' + director_seperator() + name

def create_directory(name : str) -> None:
    '''Creates a directory with the argument passed'''

    mkdir(director_seperator() + 'students' + director_seperator() + name)

def create_encrypted_file(username, filename):
    with open(final_directory(username) + filename, "w") as w:
        pass

def delete_directory(name : str) -> None:
    '''deletes the directory with the argument passed '''

    rmtree(director_seperator() + 'students' + director_seperator() + name) 

def check_if_all_directories_exists(name_list : list) -> None:
    '''Checks if all the directories for the accounts are present
                                   if not creates a new directory for it''' 

    for i in name_list:
        if path.exists(i):
            continue
        else:
            create_directory(i)

    return None

def create_encrypted_file(file : str, data : str) -> None:

    with open(director_seperator() + 'students' + director_seperator() + file, 'w') as g:
        g.write(data)

def list_all_files(way) -> list:

    return listdir(way)

def delete_a_file(name : str) -> None:
    
    remove(director_seperator() + 'students' + director_seperator() + name)

def read_encrypted_file(name : str) -> None:
    print("asd")
    