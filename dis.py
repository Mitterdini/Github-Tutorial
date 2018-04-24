print("What up nigga")
x=input("what's your favorite color: ")
def switch_demo(argument):
	switcher = {
		"green":"dang, I dig",
		"blue":"not what i'd pick but ight"}
	print(switcher.get(argument, "Invalid color"))
switch_demo(x)
