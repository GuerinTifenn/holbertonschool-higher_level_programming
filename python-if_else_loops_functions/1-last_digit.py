#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lnumb = abs(number) % 10
if number < 0:
    lnumb = lnumb * -1
if lnumb > 5:
    print(f"Last digit of {number} is {lnumb} and is greater than 5")
elif lnumb == 0:
    print(f"Last digit of {number} is {lnumb} and is 0")
else:
    print(f"Last digit of {number} is {lnumb} and is less than 6 and not 0")
