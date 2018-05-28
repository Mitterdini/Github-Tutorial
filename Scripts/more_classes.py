def os_picker(os, name):
    operating_systems = {
    "apple":Apple(name),
    "microsoft":Microsoft(name),
    "linux":Linux(name)
    }

    return operating_systems.get( os , Computer(name))

class Computer(object):

    def __init__(self, name):
        self.name = name

    def set_os(self, os):                                                       #setters; this isnt needed, but it is a homemade version
        self.os = os                                                            #you can also use setattr(object, name, value)
                                                                                #and getattr(object, name)
    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_screen(self, screen):
        self.screen = screen

class Apple(Computer):

    def __init__(self, name):
        super(Apple, self).__init__(name)                                       #Learn what super() does
        self.os = "Apple Macintosh OS"

class Microsoft(Computer):

    def __init__(self, name):
        super(Microsoft, self).__init__(name)
        self.os = "Microsoft Windows OS"

class Linux(Computer):

    def __init__(self, name):
        super(Linux, self).__init__(name)
        self.os = "Linux OS"

my_os = input("What's your computer's company?\n> ")
my_computer_name = input("What's your computer's name?\n> ")

my_computer = os_picker(my_os.lower(), my_computer_name)

print("your computer name:", getattr(my_computer, 'name'))

setattr(my_computer, 'color', 'burple')
print("your computer color:", getattr(my_computer, 'color'))

setattr(my_computer, 'gpu', 'GTX 960')
my_computer.set_cpu('Intel core I7')

print("your computer GPU:", my_computer.gpu)
print("your computer CPU:", my_computer.cpu)
print("your computer operating system:", my_computer.os)
