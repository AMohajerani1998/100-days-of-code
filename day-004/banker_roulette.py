import random

names_raw = input("Please write the names: \n")
names = names_raw.split(", ")
print(names[random.randint(0, (len(names) - 1))])