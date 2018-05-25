ten_things = "Apples Oranges Crows Telephone Light Sugar"

print(ten_things)
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
print(f"stuff: {stuff}")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))             #4th item to the 5th item, because
                                        #The first # is the position, and the
                                        #Second # is the ending cap
