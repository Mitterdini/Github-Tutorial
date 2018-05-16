float = 12.5
inte = 6
strinly = "ight"
#the 3 ways of placing a variable in a string
print(f"float: {float} ; integer: {inte}; string: {strinly}") #method 1: using 'f' before the string

print("\n\nfloat: %f ; integer: %d; string: %s" % (float,inte,strinly)) #method 2: using '%' signs

words = "lets check multiple variables using .format\n{} {} {}" #method 3; using curly brackets and .format
print(words.format(float, inte, strinly))
