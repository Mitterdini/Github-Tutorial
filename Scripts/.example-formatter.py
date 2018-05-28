#THIS ONLY WORKS IF YOU ARE IN THE DIRECTORY OF THE DESIRED FILE
from sys import argv
import subprocess

script, filename = argv

def checker(file, output):
    checking = file.read()

    if checking:
        checking = checking.replace("[1;33mmitterdiggity[0;36m> exit", "")
        checking = checking.replace("[1;33mmitterdiggity[0;36m", "mitterdiggity")
        checking = checking.replace("exit", "")
        output.write(checking)
        return checker(file, output)

target = open(filename)
new = "new_"+filename; new_target = open(new, 'w')

print("Replacing...\n")

checker(target, new_target)
target.close()
subprocess.call(["rm", "{}".format(filename)])
new_target.close()

new_target = open(new)
final = new.strip("new_"); final_target = open(final, 'w')
checker(new_target, final_target)
new_target.close()
subprocess.call(["rm", "{}".format(new)])
final_target.close()

print('Done.')
