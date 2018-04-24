import time
print('Hello')
name = input("what's your name?\n-")
time.sleep(1)
print("Ohhhhhh, my bad.\nHey, %s. What's up!" % name)
class Person:
	def __init__(self, name, age, pet):
		self.name = name
		self.age = age
		self.pet = pet
time.sleep(1)
age = input("I forgot your age. Refresh my memory?\n-")
time.sleep(1)
pet = input("I won't forget again. Wait, don't you have a pet. What was it again?\n-")
person1 = Person(name, age, pet)
time.sleep(1)
print("Well, now that that's out of the way,\n")
while(True):
	x=input(" What can i do for you?")
	print("you said it was %s"% person1.get(x))
	if(x=="nothing"):
		exit()
