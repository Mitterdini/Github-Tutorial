#THIS ONLY WORKS IF YOU ARE IN THE DIRECTORY OF THE DESIRED FILE
#use the following set a system output as a vaiable in a script:
#{      from os import popen
#       pwd = popen('pwd').read()       }
#    The above code stores the current position, however, keep in mind, this
#    adds >\n< to the end of the string set to >pwd<
#    counter act it by using >pwd.rstrip('\n')<

from sys import argv, path
from os import system
from pprint import pprint

script, filename = argv

path.extend(('/root/Coding/Python/Github/Learning-The-Hard-Way/',          # path[6]
 '/root/Coding/Python/Github/Learning-The-Hard-Way/Examples'))             # path[7]

def editor(file, output):
    checking = file.read()

    if checking:
        checking = checking.replace("[1;33mroot[0;36m> exit", "")
        checking = checking.replace("", "")
        checking = checking.replace("[1;33mroot[0;36m", "root")
        checking = checking.replace("exit", "")
        output.write(checking)
        return editor(file, output)

filename = path[6]+filename
x = filename.split('/')
name = x[-1]

target = open(filename)
new = path[6]+"new_"+name; new_target = open(new, 'w')

print("Replacing...\n")

editor(target, new_target)
target.close()
system("rm {}".format(filename))
new_target.close()

new_target = open(new)
final = new.replace(new, filename); final_target = open(final, 'w')
editor(new_target, final_target)
new_target.close()
system("rm {}".format(new))
final_target.close()

print('Done.')
