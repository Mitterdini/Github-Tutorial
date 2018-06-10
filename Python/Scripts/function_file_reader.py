from sys import argv

script, input_file = argv

def print_all(f):                           #This function reads the input variable
    print(f.read())

def rewind(f):                              #This function sets the marker to the beginning of the input variable
    f.seek(0)                               #Set offset to the beginning of the file; for more info check >pydoc file<

def print_a_line(line_count, f):            #This function prints a given number and a line of text from the file
    print(line_count, f.readline())

current_file = open(input_file)             #Set a file object

print("let's print the whole file:\n")
print_all(current_file)                     #Call print_all and with argument: current_file

print("\n\nNext lets rewind\n")
rewind(current_file)                        #Rewind current_file
print("now lets read a few lines")

current_line = 1                            #Set a line number

print_a_line(current_line, current_file)    #print a line of text from the file and it's line number
current_line += 1                           #Increment the line number
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
