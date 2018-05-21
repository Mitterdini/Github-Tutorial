from sys import argv

script, one, two, three = argv

def test(*args):                      #Use *args to set as many variables as needed like with 'argv'
    first, second, third = args       #However, with *args, it must be used in a funtion in the () symbols
    print(f"{first}{second}")
test(one, two, three)                 #Calling the function
