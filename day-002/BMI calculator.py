# formula would be weight(kg)/Height(m)**2

weight = float(input("What is your weight? "))
height = float(input("What is your height (meters)?"))
# by casting the result into an int, we can round the number up
BMI = int(weight/height**2)

print("Your BMI is " + str(BMI) + ".")