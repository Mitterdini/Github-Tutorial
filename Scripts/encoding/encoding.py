import sys                                                          # *Notice* we imported the entire sys package
script, input_encoding, error = sys.argv                            #Because we did this, we need to select where argv comes from
                                                                    #Hence, sys.argv
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)                #If line is true(as in, it reads something) then it will loop
                                                                    #to the next line

def print_line(line, encoding, errors):
    next_lang = line.strip()                                        # .strip() gets rid of useless beginning and ending spaces
    raw_bytes = next_lang.encode(encoding, errors=errors)           #what does .encode() do?
    cooked_string = raw_bytes.decode(encoding, errors=errors)       #what does .decode() do?

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")                 #why do we need [encoding="utf-8"] inside open()?

main(languages, input_encoding, error)
