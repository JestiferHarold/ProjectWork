from file_utils import *
from os_utils import *

def show_docs() -> None:
    '''used for showing the documents of other functions.'''
    clear_terminal()
    for i in functions_list:

        f = str(type(i)).strip("'<class' '").strip(">'")
        print(f"{i.__name__} = {i.__doc__} {f}")

    print(f"{show_docs.__name__} = {show_docs.__doc__} function")

show_docs()