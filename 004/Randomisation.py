# Randomisation

import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)  # prints between [0, 1)
# never prints 1
# 0.0000000... to 0.9999999......

# How to create a random decimal number between 0 and 5?
random_float1 = random.random() * 5
print(random_float1)

# Love Calculator using randomisation
Love_score = random.randint(1, 100)
print(f"Your Love Score is {Love_score}.")

