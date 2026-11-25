# formula would be weight(kg)/Height(m)**2

weight = float(input("What is your weight? kg "))
height = float(input("What is your height? cm "))
# by casting the result into an int, we can round the number up
height_meters = height/100
bmi = round(weight/height_meters**2)

print("Your BMI is " + str(bmi) + ".")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are slightly overweight.")
elif 30 <= bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")