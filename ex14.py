# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex14.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisul <rahisul@icloud.com>                   / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2018/10/06 17:08:47 by rahisul          /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2018/10/06 17:23:35 by rahisul                                                  #
#                                                                                             #
# ******************************************************************************************* #

from sys import argv

script, user_name = argv 
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you some questions.")
print(f"Do you like me {user_name}? ")
like = input(prompt)

print(f"Where do you live {user_name}?")
live = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {like} about liking me, 
You live in {live}, not sure where that is,
And you have a {computer}. Nice!
""")

