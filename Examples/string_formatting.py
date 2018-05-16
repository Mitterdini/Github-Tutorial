float = 12.5
inte = 6
strinly = "ight"
print(f"float: {float} ; integer: {inte}; string: {strinly}")
print("\n\nfloat: %f ; integer: %d; string: %s" % (float,inte,strinly))

words = "lets check multiple variables using .format\n{} {} {}"
print(words.format(float, inte, strinly))
