#strings
#subscripting is used to pull a character from a string, and the first character starts from 0 and goes +1 forward
print("Hello"[0])
print("Hello"[4])

print("123" + "456")

#Integers

print(123 + 456)
#adding _ in between numbers works the same as , to indicate ever group of 3 for better reading
print(111_111_111 + 222_222_222)

#Float

print(3.12 + 3.1)

#Boolean

True
False

# len function always works with strings and not integers

#to get the type of a variable we use type()
name_len = len(input("Enter your name: "))
#name_len_report = "The length of your name is " + name_len + " characters"
#print(name_len_report)
# the concatenation only works on strings, and we cannot concatenate an int with a string
#so we cast the int variable into str
name_len_report = "The length of your name is " + str(name_len) + " characters"
print(name_len_report)

#we can cast the int into a float as well
new_name_len = float(name_len)
print(new_name_len)
