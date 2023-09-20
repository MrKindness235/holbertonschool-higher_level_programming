#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=" ")
number = number % 10
print (f"{number}", end=" ")
if number > 5:
    print(f"and is greater than 5")
elif number == 0:
    print(f"and is 0")
elif number < 6 and number != 0:
    print(f"and is less than 6 and not 0")
