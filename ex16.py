# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex16.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisul <rahisul@icloud.com>                   / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2018/10/06 17:46:14 by rahisul          /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2018/10/06 18:14:46 by rahisul                                                  #
#                                                                                             #
# ******************************************************************************************* #

from sys import argv

script, filename = argv 

print(f"I am going to erase {filename}.")
print("If you don't want to do this hit CRTL-C (^C).")
print("If you do want that, hit RETURN.")

input(">")

print("Opening the file")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("Now, I'm going to ask you for the three names of those girls you had crush on?")
name1 = input("Name 1:")
name2 = input("Name 2:")
name3 = input("Name 3:")

print("I'm going to write thses name to the file!")
target.write(name1)
target.write("\n")
target.write(name2)
target.write("\n")
target.write(name3)
target.write("\n")

print("And finally we are closing the file!")
target.close ()



file_again = input("Type you file name again..")
target_again = open(file_again)
print(target_again.read())
target_again.close()
