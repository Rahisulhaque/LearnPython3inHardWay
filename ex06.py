# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex06.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisul <rahisul@icloud.com>                   / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2018/10/06 14:47:15 by rahisul          /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2018/10/06 14:57:35 by rahisul                                                  #
#                                                                                             #
# ******************************************************************************************* #

types_of_people = 10 
x = f"There are {types_of_people} types of people"

binary = "Binary"
donot = "don't"

y = f"Those who are {binary} and those who {donot}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "This is the right side of ..."

print(w + e)

# In this exercise I have learnt .format() method
