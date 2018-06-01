from os import system
from time import sleep

def title_screen():
    system('clear')
    print("\n\n\n\n\n\t\t\t\v\vTHE LINK OF LEGEND")
    input("\n\n\n\n\n\n\n\n\t\t     (press enter to continue)")
    system('clear')

def main_menu():

    print("""
            THE LINK OF LEGEND

            \t    Start
            \t    Load
            \t    Settings
            \t    Quit""")
    choice = input("select: ")
    menu = {
        'start': start,
        'load': load.failure,
        'settings': settings.failure,
        'quit': quit,
        }

    menu[choice]() if choice in menu else fail()

def fail():
    system('clear')
    print("\t\v\vPlease choose one of the available options")
    sleep(2)
    system('clear')
    main_menu()

class Failed(object):

    def failure(self):
        system('clear')
        print("\t\v\vThis function has yet to be implemented")
        input("\t\t\vpress enter to continue")
        system('clear')
        main_menu()

def quit():
    system('clear')
    print('\t\t\t Thanks for playing!!!\n\t\t\t\tBye<3')
    exit(0)

def start():
    print('\t\t\t\v\vAnd so your journey begins\n\n')

def startup():
    title_screen()
    main_menu()

load = Failed()
settings = Failed()
