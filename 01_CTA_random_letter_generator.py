# Collect Them All Component 1 - Generate a random list of chosen letters

import random

letters = ["C","O","F","E"]

for item in range(0,20):
    chosen_letters = random.choice(letters)
    print(chosen_letters)