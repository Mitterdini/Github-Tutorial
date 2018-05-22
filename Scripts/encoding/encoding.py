import sys                                                          # *Notice* we imported the entire sys package
script, input_encoding, error = sys.argv                            #Because we did this, we need to select where argv comes from
                                                                    #Hence, sys.argv
def main(language_file, encoding, errors):
    line = language_file.readline()                                 #keep in mind, .readline() has a natural '\n' at the end of it

    if line:                                                        #This keeps the function loop from looping forever because it
        print_line(line, encoding, errors)                          #will only loop if *line* has something in it
        return main(language_file, encoding, errors)                #If *line* is true(as in, it reads something) then it will loop
                                                                    #and run main() again; thus cycling through the file

def print_line(line, encoding, errors):
    next_lang = line.strip()                                        # .strip() gets rid of the natural '\n' thats at the end of *line* variable
    raw_bytes = next_lang.encode(encoding, errors=errors)           # String + .encode() = Bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)       # Bytes + .decode() = String
                                                                    #DBES --> Decode Bytes Encode Strings
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")                 #why do we need [encoding="utf-8"] inside open()?

main(languages, input_encoding, error)
