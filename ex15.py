# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex15.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisul <rahisul@icloud.com>                   / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2018/10/06 17:30:21 by rahisul          /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2018/10/06 17:44:59 by rahisul                                                  #
#                                                                                             #
# ******************************************************************************************* #

from sys import argv 
script, filename = argv

txt = open(filename)

print(f"Here is your {filename}")
print(txt.read())
txt.close()

print(f"Okay! Type your filename again: ")
file_again = input('>')

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
