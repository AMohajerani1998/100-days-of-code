# there are about 52 weeks in a year
age = int(input("Enter your age: "))

# assuming humans live up to age of 90
years_left = 90 - age

# weeks left
weeks_left = years_left * 52

print(f"You have {str(weeks_left)} left. Enjoy!")