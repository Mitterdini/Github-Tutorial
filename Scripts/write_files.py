from sys import argv                                #Import the argument module
import os                                           #Allows for terminal commands

script, filename = argv                             #Set script name and gets the target file name from the terminal command

print(f"""\nThis script will erase the file
to proceed type 'y'
press anything else to cancel\n""")

confirm = input(f"What's it gunna be, gorgeous?\nDelete {filename}? (y/n)\n> ") #Making sure they're ready to erase the script
os.system('clear')
print("Onward!!") if confirm == 'y' else exit()

print("\nWelp, let's get to it then.\nOpening the file...")
target = open(filename, 'w')                        #Opening the file in write mode
#There is 'w' for write; 'r' for read; and 'a' for append modes

print(f"\nTruncating the file, A.K.A.\nTime for {filename} to meet Thanos")     #Infinity War Reference
target.truncate()

text = input("Soowa, what's it gunna be. Whatcha wanna write?\n> ")             #User input's what they would like to write to {filename}

print("\nExcellence!!\nAlright Mr.Businessman, let's write it to the file")

target.write(text)                                              #Script writes {text} to the file
target.write('\n')                                              #So each input is a new line

again = input("Do you wanna write more? (y/n)\n> ")
cont = True if again == 'y' else target.close()                 #Checker if you want to write more, otherwise, close the file

while(cont == True):                                            #Loop to write as much as you like
    os.system('clear')
    text = input("What else you wanna write?\n> ")
    target.write(text)
    target.write('\n')

    again = input("write more? (y/n)\n> ")
    cont = True if again == 'y' else target.close()             #ALWAYS REMEMBER TO CLOSE THE FILE
