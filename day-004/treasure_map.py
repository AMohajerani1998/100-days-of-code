line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
treasure_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ").lower()

column = position[0]
columns = ["a", "b", "c"]
if column in columns:
    column = columns.index(column)
else:
    print("Bad input! retry...")
row = (int(position[1]) -1)

treasure_map[row][column] = "X"

print(f"{line1}\n{line2}\n{line3}")
