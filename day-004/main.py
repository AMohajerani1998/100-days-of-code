# To be able to use random generator, we import the random module first
import random

print(random.randint(1, 6))

# To import our own modules, we first create the module file, and then import it:
import my_module
print(my_module.a)

# To print a random float between 0 and 1.0:
print(random.random())

#print(round((random.randint(0, 500)/100), 3))
print(random.random()*5)

