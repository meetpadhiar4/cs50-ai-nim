import random

actions = [(0, 1), (1, 1), (0, 2)]
weights = [0.9, 0.1, 0.1]
choice = random.choices(actions, weights=weights)[0]
print(choice)
