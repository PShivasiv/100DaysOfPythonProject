# This programe take the input the names of the memeber and random choice one of them which will gonna pay the bill
import random
name_string=input("Give me the everyone name seprated by a comma.\n")
name=name_string.split(",")
name_items = len(name)
pick=random.randint(0, name_items-1)
print(name[pick] +" is going to buy the meal today")
