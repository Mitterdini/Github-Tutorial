print("What up nigga")
x=input("what's your favorite color: ")
def switch_demo(choice):
	switcher = {
		"green":"dang, I dig",					 #Dictionaries use {Key:Value}
		"blue":"not what I'd pick but ight"}	 
	print(switcher.get(choice, "Invalid color")) #.get has a built in error slot
												 #example.get(arg, "error MSG")
switch_demo(x)
