#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if number < 0:
    ld = ((number * -1) % 10) * -1
    print(f"Last digit of {number} is {ld}", end=" ")
else:
    print(f"Last digit of {number} is {ld}", end=" ")

if ld == 0:
    print("and is 0")

elif ld < 6 and ld != 0:
    print("and is less than 6 and not 0")

else:
    print("and is greater than 5")
