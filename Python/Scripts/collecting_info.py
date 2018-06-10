from sys import  argv

name, user = argv                                                   #Getting info from the terminal original command
prompt = 'You said: '                                               #Setting the input name

print(f"ayo {user}, what's up? I'm {name}. nice to meetcha")
print("I got a few questions foryas.")
print("what foods do you like?")
likes = input(prompt)                                               #User inputs data

print(f"soowa, where you from?")
home = input(prompt)                                                #User inputs data

print("what kinda build you got?")
Computer_build = input(prompt)                                      #User inputs data
                                                                    #Outputting the gathered information
print(f"""
welp, imma go hack ya cheeks now.
your name is {user}
your favorite food is {likes}
you're from {home}
and you got a {Computer_build}
""")
