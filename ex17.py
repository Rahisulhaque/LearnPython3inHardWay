# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex17.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisul <rahisul@icloud.com>                   / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2018/10/06 18:19:15 by rahisul          /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2018/10/06 18:39:40 by rahisul                                                  #
#                                                                                             #
# ******************************************************************************************* #

from sys import argv
from os.path import exists

script, from_file, to_file = argv 
print(f"Copying file {from_file} to {to_file}...")

in_file = open(from_file, 'r')
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")
print("Ready, hit RETURN to continue, CRTL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done!")
out_file.close()
in_file.close()
