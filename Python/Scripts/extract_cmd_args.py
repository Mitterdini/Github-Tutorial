from sys import argv                    #This imports the arguments from a bash command

script_name, first_arg, second_arg, third_arg = argv     #This line extracts 4 arguments; 1-> The name of the file; 2-> The first following argument
                                                    #3-> The second following argument; 4-> The third argument from the bash command
                        #Print the arcuments
print(f"script_name = {script_name} \nfirst argument = {first_arg} \nsecond argument = {second_arg} \nthird argument = {third_arg}")
