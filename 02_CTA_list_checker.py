# Collect Them All Component 2 - check that there are enough of each letter in the list

import random

op = "n"
letters = ["C","O","F","F","E","E"]
checker = []

for i2 in range(0,3):
    chosen_letters = random.choice(letters)
    print(chosen_letters)
    checker.append(chosen_letters)

for i in range(0,6):
    item = 0
    letter = letters[item]
    while checker.count(letter) == 0:
        try:
            isinstance(checker.index("C"), int)

        except ValueError:
            continue

    item += 1
