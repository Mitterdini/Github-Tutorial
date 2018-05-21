from sys import argv                        #Import the argv module
from os.path import exists                  #Import the exists module -> tells if a file exists or not.

script, from_file, to_file = argv           #Gets info from Terminal

print(f"Copying from {from_file} to {to_file}\n")

in_file = open(from_file); indata = in_file.read()              #Sets a file object; Reads the initial file

print(f"The input file is {len(indata)} bytes long")

print(f"Does an output file exist?\t~{exists(to_file)}\n")      #Tells if the target file exists or not
input("press RETURN to continue, or CTRL-C (^C) to cancel")     #If True, it just adds to the file
                                                                #If False, it creates a file and copies to it
out_file = open(to_file,'w')                                    #Sets a file object in write mode
out_file.write(indata)                                          #Writes the contents of the initial file to the target file

print("\n\nAaaaaaaaaaaaaand, Finished!!")
out_file.close(); in_file.close()                               #DON'T FORGET TO CLOSE ALL FILES
