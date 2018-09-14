clap = 5
dat = "pass"

dict = {"succ":"is short for succle", clap:dat, 7: 45}                          #You ca set variables, strings, or numbers
x = input("pick something: ")
print(dict.get(x),"\n")                                                         #This only works with strings => conversions don't count.

print("""\nwhen using a variable you need to call the variable
not what it's assigned to:""", dict.get(clap))                                  #This works when the variable is predefined
print("\n")

dict["Tom"] = "Is a female dog"                                                 #Another way to add keys/balues to a dictionary
dict[3] = "Musketeers"
dict["two"] = 2                                                                 #REMEMBER keys are case-sensitive

print(dict, "\n")                                                               #Printing values
print(dict.get("Tom"))                                                          #User input may not be able to call variable/numbered keys
print(dict.get(3))                                                              #But you can still call them using >example.get('key')<
print(dict.get("two"))

#You can send an error message if a key is not in a dictionary
print('\n', dict.get(5,"ERROR: Not even close."))                                      #Watch out because assigned variable values hold the same
print(dict.get(8, "ERROR: numbers are neat right!!"))
print(dict.get("goof", "ERROR AGAIN: welp, still wrong"))
