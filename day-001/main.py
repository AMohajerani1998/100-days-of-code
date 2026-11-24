print("Hello world!")
print("She said: \"Hello\" and left.")
print('She said: "Hello" and left.')

print("\nHello world!\nHello world!\nHello world!\n")

print("Hello" + " " + "world!")

# Printing a string along with whatever is entered along with input
print("Your name is: " +input("What is your name?\n") + "\n\n")

# Putting whatever is entered as input as a variable:
name = input("What is your name?\n")
print("Hello " + name + "\n\n")

# variable can be updated throughout the code by assigning new values to it

name2 = "Jack"
print (name2)
name2 = input("What is your name?\n")
print ("Your name: " + name2 + "\n\n")

# len function prints out the length of a string
# probably the new python requires the value to always be turned into string so we have to use str function too
print("name length: " + str(len(name2)))