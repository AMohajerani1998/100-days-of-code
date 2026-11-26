# Rollercoaster
print("Welcome to the rollercoaster!")
height = int(input("Enter your height: cm "))
age = int(input("Enter your age: "))

if height >= 120 and 55 >= age >= 45:
    print("The fee is $0.")
elif height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("The fee is $5.")
    elif 12 <= age <= 18:
        print("The fee is $7.")
    else:
        print("The fee is $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# comparison operators include == != >= <=
