# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex18.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisul <rahisul@icloud.com>                   / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2018/10/06 18:42:45 by rahisul          /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2018/10/06 19:11:26 by rahisul                                                  #
#                                                                                             #
# ******************************************************************************************* #

def print_two (*args):
    arg1, arg2 = args
    print(f"arg 1: {arg1}, arg 2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"args  are{arg1} and {arg2}.")

def print_one(arg):
    print(f"The arg  1 is {arg}.")

def print_nothing():
    print("Nothing")

print_two("Audrey", "Winter")
print_two_again("Drey", "Winters")
print_one("Audrey")
print_nothing()
