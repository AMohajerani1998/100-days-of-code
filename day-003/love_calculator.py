print("The Love Calculator is calculating your score...")
name1 = input("What is your name?").lower()
name2 = input("What is their name?").lower()
combined_names = name1 + name2
score1 = 0
score1 += combined_names.count("t")
score1 += combined_names.count("r")
score1 += combined_names.count("u")
score1 += combined_names.count("e")

score2 = 0
score2 += combined_names.count("l")
score2 += combined_names.count("o")
score2 += combined_names.count("v")
score2 += combined_names.count("e")

total = int(str(score1) + str(score2))

if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go together like coke and mento!")
elif (total > 40) and (total < 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")