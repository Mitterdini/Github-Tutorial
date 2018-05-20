from sys import argv                 #Import the argv module

script_name, filename = argv         #Grabs the script name and filename

txt = open(filename)                 #Creating a file object

print(f"Okidoki, I'm going to find {filename} now...\nWorking...")
print(f"Here's what I found:\n\n{txt.read()}")                  # >txt.read()< where {txt} is our set variable// this shows what's in the selected file

again = input("would you like to read a new file? (y/n)\n> ")   #Asking if you would like to seach anonther file
cont = True if again == 'y' else txt.close()                    #A quick checker before implementing the loop

while(cont == True):                                            #Rinse and repeat
    filename = input("What's the new file's name?\n> ")
    txt = open(filename)

    print("Output:\v\v", txt.read())

    again = input("would you like to read a new file? (y/n)\n> ")
    cont = True if again == 'y' else txt.close()      #Don't forget to close file's when youre done!!!
