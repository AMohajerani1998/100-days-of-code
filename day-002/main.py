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

### logical operators
# parathesis (), Exponent **, Multiplication *, Division /, Addition +, Substraction -
#logical operators go in the order of PEMDAS left to right that is () ** * / + -

print(3 * 3 + 3/3 - 3)
# addition of a float and integer always results into a float

print(3*(3+3)/3-3)

### rounding up the results
# to round up the results the easy way is to cast it into an int, but we can also use the round() function
print(8/3)
# the default result is an int
print(round(8/3))
print(type(round(8/3)))
print(round((8/3), 2))
# another way is to use // which would show the int value of the result
print(9//2)

# we also can use -= or += and so on for each operation instead of using the same variable to reassign a new value to it after addin an operation to it
result = 4/2
#result = result / 2
result /= 2
print(result)

### f-strings
# Instead of using "" + ... we can use f"" to be able to put our variable values in {} for better and faster pace
score = 0
score += 1
print(f"Your score is {score}.")

