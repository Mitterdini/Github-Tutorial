from os import system
from time import sleep

def title_screen():
    print("THE LINK OF LEGEND")
    input("\n\n(press enter to continue)")
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

    load = Failed()
    settings = Failed()

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
    print('\t\t\t Thanks for playing!!!\vBye<3')
    exit(0)

def start():
    
