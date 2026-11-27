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

# Lists are shown as follows:
fruits = ["apple", "orange", "peach"]

# Showing items from lists:
print(fruits[0])
# Can work in reverse order to show the last item:
print(fruits[-1])

# Changing items in the list:
fruits[0] = "pear"
print(fruits)

# Appending to the list:
fruits.append("apple")
print(fruits)

# Adding two lists together:
veggies = ["greens", "cucumber", "brocoli"]
fruits.extend(veggies)
print(fruits)

# removing the last member of the list or given a position, that position:
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

# removing a value from the list:
fruits.remove("peach")
print(fruits)

# clearing a list:
veggies.clear()
print(veggies)

# Number of items in a list
print(len(fruits))

# inserting an item in a list at a position without removing the previous item at the said position
fruits.insert(3, "peach")
fruits.insert(5, "peach")
print(fruits)

# position of a value (in case of multiple items with the same value, the first one will be said)
print(f"index of \"peach\": {fruits.index("peach")}")

# count the number of items with the indicated value:
print(fruits.count("peach"))

# boolean return of a value being in a list or not:
print("peach" in fruits)

# sorting a list alphabetical or numerical (can be in reverse if indicated):
fruits.sort()
print(fruits)

# reverse the order already placed for a group:
fruits.reverse()
print(fruits)

# joining two lists without changing any of them
fruits2 = ["banana", "coconut"]
all_fruits = fruits + fruits2
print(all_fruits)