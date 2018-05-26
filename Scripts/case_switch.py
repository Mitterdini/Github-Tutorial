print("What up bruv?")
x=input("what's your favorite color: ")
def switch_demo(choice):
	switcher = {
		"green":"Dang, I dig",					 #Dictionaries use {Key:Value}
		"blue":"Not what I'd pick, but ight"}
	print(switcher.get(choice, "Invalid color")) #.get has a built in error slot
												 #example.get(arg, "error MSG")
switch_demo(x)
