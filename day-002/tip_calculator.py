print("Welcome to the tip calculator!")
bill = float(input("How much was the total bill? €"))
tip = int(input("How much would you like to tip? %"))
people = int(input("How many people to split the bill? "))

#tip2 = int(f"1.{tip}")
#print(tip2)

result = round((bill + (bill * tip/100))/people, 2)
# another method to round up: result = "{:.2f}".format(result)
print(f"Each person has to pay €{result}.")