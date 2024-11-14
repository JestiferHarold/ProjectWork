from time import *
from os_utils import *
from platform import *

def decorator1(page_name : str,asd : str) -> None:

    '''This function is used for decorating'''
    
    clear_terminal()
    print(f"{asd} Moving to {page_name} page")
    sleep(3)
    clear_terminal()


def basic_decorator() -> None:

    '''This function is used for decorating'''

    sleep(3)
    clear_terminal()

def decorator_for_quiting(q : str) -> None:

    '''This function is used for decorating'''

    sleep(1)
    clear_terminal()
    print(f"{q} the program in")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(0.5)