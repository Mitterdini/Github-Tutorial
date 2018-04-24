import time
import os

os.system('clear')
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
os.system('clear')
print("Well, now that that's out of the way,\n")
answers = {"age":person1.age, "pet":person1.pet, "name":person1.name}
while(True):
	y=input("What can I do for you?\n-")
	if(y=="nothing"):	exit()
	elif(y not in answers):
		print("please be more specific")
	else:
		print("you said it was %s"% answers[y])
	time.sleep(2)
	os.system('clear')
