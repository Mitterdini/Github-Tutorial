from os import system, path, popen, listdir

pwd = "/root/Coding/Python/Github/Learning-The-Hard-Way/Projects/.NewProject/"

log_name = f"{pwd}logs/log_entry.txt"

all = popen("ls -A /root/Coding/Python/Github/Learning-The-Hard-Way/Projects/.NewProject/logs/*").read()
all = all.split('\n')
all.remove('')

if len(listdir('/root/Coding/Python/Github/Learning-The-Hard-Way/Projects/.NewProject/logs/')) == 0:
    pass
elif(all[0] == log_name):
    log_num = 0
else:
    log_num = all[0]
    log_num = log_num.lstrip('/root/Coding/Python/Github/Learning-The-Hard-Way/Projects/.NewProject/logs/log_entry-')
    log_num = log_num.rstrip('.txt')

if (path.isfile(log_name) == True):
    log_num = int(log_num) + 1
    log_name = log_name.rstrip('.tx')
    log_name = log_name + '-' + str(log_num) + '.txt'
else:
    pass

print("Creating uninstall log...")
system(f"python3 {pwd}setup.py install --record {pwd}Files_To_Be_Uninstalled.txt | tee {log_name}")
system(f'echo "the uninstalled files:  " >> {log_name}')
system(f'cat {pwd}Files_To_Be_Uninstalled.txt >> {log_name}')
system(f"cat {pwd}Files_To_Be_Uninstalled.txt | xargs rm -fr")
system(f"rm -f {pwd}Files_To_Be_Uninstalled.txt")
print("Finishing up...")
