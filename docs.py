from file_utils import *
from os_utils import *
from main import *

functions_list = [
    quit,
    init,
    init_option_matcher,
    logging,
    forgot_password,
    creating_an_account,
    deleting_an_account,
    Dashboard,
    Dashboard_option_matcher,
    account_settings,
    inv_pass,
    inv_user,
    account_settings_option_matcher,
    encrypting,
    decrypting,
    deleting_files,
    create_directory,
    delete_directory,
    check_if_all_directories_exists,
    password_strength,
    check_if_email_exists,
    check_if_username_exists,
    create_base_binary_file,
    create_account,
    read_binary_file,
    delete_account,
    change_password,
    change_username,
    clear_terminal,
    fun,
    decrypt,
    bets1,
    bets2,
    git,
    space,
    special,
    texties,
    decorator1,
    basic_decorator,
    decorator_for_quiting
]

def show_docs() -> None:
    '''used for showing the documents of other functions.'''
    clear_terminal()
    for i in functions_list:

        f = str(type(i)).strip("'<class' '").strip(">'")
        print(f"{i.__name__} = {i.__doc__} {f}")

    print(f"{show_docs.__name__} = {show_docs.__doc__} function")

show_docs()